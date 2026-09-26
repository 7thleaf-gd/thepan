# THE PAN CURRENT

Status: CURRENT
Authority: `7thleaf-gd/thepan`
Production branch: `main`
Production hostname: `thepan.xyz`
Deploy provider: Cloudflare Pages

## Canonical deploy path

```text
GitHub main
  -> Cloudflare Pages Git integration
  -> npm run build
  -> dist/
  -> thepan.xyz
```

## Fixed rules

- Normal deploy is the simple path above.
- Push / merge to `main` is the production deploy trigger.
- No CircleCI deploy path.
- No GitHub Actions deploy path.
- No `gh-pages` production path. The branch is legacy only and must not be synchronized or used for release.
- No local / DC / RDC dependency for normal deploys.
- No manual trigger commits.
- Do not invent an additional deploy lane.
- Production closeout requires readback from `https://thepan.xyz/`.

## Build contract

- Build command: `npm run build`
- Output directory: `dist/`
- Build implementation: `scripts/build.mjs`

## Current source

- Latest intended source: `main`
- UI change: PR #20 — thin `FIVE WAYS IN` sitemap before the footer.
