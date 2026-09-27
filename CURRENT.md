# THE PAN CURRENT

Status: CURRENT
Authority: `7thleaf-gd/thepan`
Deploy authority: CircleCI
Production branch: `main`
Production hostname: `thepan.xyz`
Provider: Cloudflare Pages
Project: `thepan`

## Canonical deploy path

```text
GitHub main
  -> CircleCI
  -> npm run build
  -> CircleCI OIDC
  -> account-switch-bridge / Cloudflare MAIN credential
  -> Cloudflare Pages / thepan
  -> thepan.xyz
  -> production readback
```

## Fixed rules

- CircleCI is the only normal production deploy executor.
- Pages deploy does not consume the `7thleaf-studios-deploy` credential context.
- CircleCI authenticates to `account-switch-bridge` by OIDC.
- Cloudflare MAIN credential remains only in the bridge; it is not copied into this repository or CircleCI.
- `scripts/pages-relay-deploy.py` is the sole Pages transport client.
- Cloudflare Git Integration is not the production authority.
- GitHub Actions and `gh-pages` are not production deploy paths.
- Direct Cloudflare API-token/Global-Key deployment from this repository is not a production executor.
- No local / DC / RDC dependency for normal deploys.
- DC is repair/recovery only.
- No direct Wrangler/API-token deploy, Cloudflare Git Integration, GitHub Actions deploy, Mac/DC deploy, or second relay may be added beside this path.
- Production is complete only after readback from `https://thepan.xyz/` passes.

## Current UI target

- `FIVE WAYS IN` is a quiet single-row sitemap before the footer.
- No giant five-card version.
- No long descriptive copy above that sitemap.
