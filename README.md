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
  -> Cloudflare Pages direct upload
  -> thepan
  -> https://thepan.xyz/
  -> production readback
```

Deployment authority is `.circleci/config.yml` using CircleCI context `7thleaf-studios-deploy`.

### Locked rules

- Normal deploys use only CircleCI -> Cloudflare Pages.
- `CLOUDFLARE_API_TOKEN` is the only Cloudflare production credential used by the deploy job.
- Global API Key is not a production credential and must not be stored in CircleCI.
- Cloudflare Git Integration is not the production deploy authority.
- GitHub Actions / `gh-pages` are not production deploy paths.
- Account Switcher is not a production deploy path.
- Mac / DC / RDC is recovery only and must not be required for normal deploys.
- Do not add another production executor without explicitly replacing this authority.
- A deploy is incomplete until live readback from `https://thepan.xyz/` passes.
