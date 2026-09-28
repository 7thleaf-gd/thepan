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

- CircleCI is the only normal production deploy executor.
- CircleCI context: `7thleaf-studios-deploy`.
- Cloudflare credential: scoped `CLOUDFLARE_API_TOKEN` only.
- Global API Key must not be stored as a deploy credential.
- Cloudflare Git Integration is not the production authority.
- GitHub Actions and `gh-pages` are not production deploy paths.
- Account Switcher is not a deployment executor.
- No local / DC / RDC dependency for normal deploys.
- DC is repair/recovery only.
- No alternate deploy lane may be added beside this path.
- Production is complete only after readback from `https://thepan.xyz/` passes.

## Current UI target

- `FIVE WAYS IN` is a quiet single-row sitemap before the footer.
- No giant five-card version.
- No long descriptive copy above that sitemap.

## Chappy 0002 production verification

- Executor trace: `CHAPPY-0002-GD-DEPLOY-20260929-THEPAN`
- Shared CircleCI context: `7thleaf-studios-deploy`
- Shared Cloudflare credential was replaced with a long-lived CI API token before this verification run.
- Verification target: CircleCI deploy -> `https://thepan.xyz/` -> production readback.
