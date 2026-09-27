#!/usr/bin/env python3
import base64
import json
import mimetypes
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

from blake3 import blake3

BRIDGE = "https://account-switch.7thleaf.xyz/execute"
CF_API = "https://api.cloudflare.com/client/v4"
PROJECT = os.environ.get("CF_PAGES_PROJECT", "").strip()

def post_json(url, token, payload):
    req = urllib.request.Request(
        url,
        data=json.dumps(payload, separators=(",", ":")).encode(),
        headers={
            "authorization": "Bearer " + token,
            "content-type": "application/json",
            "accept": "application/json",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/140.0 Safari/537.36",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=45) as response:
            return json.loads(response.read().decode())
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode(errors="replace")
        raise RuntimeError(f"HTTP {exc.code} {url}: {detail[:1200]}") from exc

def bridge(token, action, payload):
    data = post_json(BRIDGE, token, {
        "service": "cloudflare",
        "target": "MAIN",
        "action": action,
        "payload": payload,
    })
    if not data.get("ok"):
        raise RuntimeError("bridge " + action + " failed: " + json.dumps(data)[:1500])
    return data

def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: pages-relay-deploy.py <publish-dir>")
    if PROJECT not in {"7thleaf-studios", "thepan"}:
        raise SystemExit("CF_PAGES_PROJECT must be 7thleaf-studios or thepan")
    root = Path(sys.argv[1])
    oidc = os.environ.get("CIRCLE_OIDC_TOKEN_V2") or os.environ.get("CIRCLE_OIDC_TOKEN")
    if not oidc:
        raise SystemExit("CircleCI OIDC token missing")

    manifest = {}
    assets = {}
    headers_text = ""
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(root).as_posix()
        if rel == "_headers":
            headers_text = path.read_text()
            continue
        raw = path.read_bytes()
        encoded = base64.b64encode(raw).decode()
        ext = path.suffix[1:] if path.suffix else ""
        digest = blake3((encoded + ext).encode()).hexdigest()[:32]
        mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        manifest["/" + rel] = digest
        assets[digest] = {
            "key": digest,
            "value": encoded,
            "metadata": {"contentType": mime},
            "base64": True,
        }

    upload = bridge(oidc, "get_pages_upload_token", {"project_name": PROJECT})
    jwt = upload["jwt"]
    hashes = list(assets.keys())

    missing_response = post_json(CF_API + "/pages/assets/check-missing", jwt, {"hashes": hashes})
    if missing_response.get("success") is False:
        raise RuntimeError("check-missing failed: " + json.dumps(missing_response)[:1500])
    missing = missing_response.get("result", [])
    if not isinstance(missing, list):
        raise RuntimeError("unexpected check-missing response: " + json.dumps(missing_response)[:1500])

    if missing:
        upload_body = [assets[h] for h in missing]
        uploaded = post_json(CF_API + "/pages/assets/upload", jwt, upload_body)
        if uploaded.get("success") is False:
            raise RuntimeError("asset upload failed: " + json.dumps(uploaded)[:1500])

    upsert = post_json(CF_API + "/pages/assets/upsert-hashes", jwt, {"hashes": hashes})
    if upsert.get("success") is False:
        raise RuntimeError("upsert-hashes failed: " + json.dumps(upsert)[:1500])

    commit_hash = os.environ.get("CIRCLE_SHA1", "")
    deployed = bridge(oidc, "create_pages_deployment", {
        "project_name": PROJECT,
        "manifest": manifest,
        "headers_text": headers_text,
        "branch": "main",
        "commit_hash": commit_hash,
        "commit_message": "7thleaf CircleCI cloud deploy",
        "commit_dirty": "false",
    })
    print("PAGES_RELAY_DEPLOY=PASS")
    result = deployed.get("result", {})
    if isinstance(result, dict):
        envelope = result.get("result", {})
        if isinstance(envelope, dict):
            print("DEPLOYMENT_ID=" + str(envelope.get("id", "")))

if __name__ == "__main__":
    main()
