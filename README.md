# THE PAN

Production one-page site for `thepan.xyz`.

```sh
npm run dev
```

Open `http://localhost:5174/`.

Build the static output:

```sh
npm run build
```

## Canonical deployment

```text
GitHub main
  -> CircleCI
  -> npm run build
  -> CircleCI OIDC -> account-switch-bridge (credential broker)
  -> Cloudflare Pages
  -> thepan
  -> https://thepan.xyz/
  -> production readback
```

Deployment authority is `.circleci/config.yml` using CircleCI context `7thleaf-studios-deploy`.

### Locked rules

- Normal deploys use only CircleCI -> Cloudflare Pages.
- CircleCI does not store the Cloudflare MAIN credential for Pages.
- CircleCI authenticates to `account-switch-bridge` with OIDC; the bridge is credential custody only, not a second deploy executor.
- `scripts/pages-relay-deploy.py` is the sole Pages transport client for this repository.
- Cloudflare Git Integration is not the production deploy authority.
- GitHub Actions / `gh-pages` are not production deploy paths.
- Direct Cloudflare API-token/Global-Key deployment from this repository is not a production deploy path.
- Mac / DC / RDC is recovery only and must not be required for normal deploys.
- Do not add direct Wrangler/API-token deploy, Cloudflare Git Integration, GitHub Actions deploy, or another relay beside this path.
- A deploy is incomplete until live readback from `https://thepan.xyz/` passes.
