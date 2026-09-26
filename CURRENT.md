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
  -> wrangler pages deploy dist
  -> Cloudflare Pages / thepan
  -> thepan.xyz
  -> production readback
```

## Fixed rules

- CircleCI is the production deploy authority.
- GitHub Actions is not used for normal production deploys.
- GitHub-hosted runners are not required.
- `gh-pages` is legacy and not the production authority.
- No local / DC / RDC dependency for normal deploys.
- No alternate deploy lane may be invented.
- Production is complete only after readback from `https://thepan.xyz/` passes.

## Current UI target

- `FIVE WAYS IN` is a quiet single-row sitemap before the footer.
- No giant five-card version.
- No long descriptive copy above that sitemap.
