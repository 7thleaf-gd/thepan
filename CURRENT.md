# THE PAN CURRENT

Status: CURRENT
Authority: `7thleaf-gd/thepan`
Source branch: `main`
Production publish branch: `gh-pages`
Production hostname: `thepan.xyz`

## Canonical deploy path

```text
GitHub main
  -> static production files
  -> direct sync to gh-pages via GitHub API
  -> GitHub Pages
  -> thepan.xyz
```

## Fixed rules

- This project uses the simple static deploy path above.
- No CircleCI deploy dependency.
- No GitHub Actions workflow dependency.
- No local / DC / RDC dependency.
- No manual empty trigger commits.
- Do not assume Cloudflare Pages Git integration unless it is independently verified.
- `gh-pages` is the active publish surface while GitHub Pages remains enabled.
- Production closeout requires the publish files on `gh-pages` to match the intended `main` static output.

## Build contract

- Build command: `npm run build`
- Output directory: `dist/`
- Build implementation: `scripts/build.mjs`
- Current site is static; deploy only the production output that changed.

## Current deployment evidence

- GitHub repository reports Pages enabled.
- Latest UI change: PR #20 — thin `FIVE WAYS IN` sitemap before the footer.
- Production sync performed for `index.html` and `styles-v2.css`.
- `main` and `gh-pages` blob SHAs match for both changed production files.
