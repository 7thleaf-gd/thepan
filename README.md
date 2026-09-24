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

Pushes to `main` deploy through the Cloudflare Pages Git integration.

Production deploy path: GitHub `main` → Cloudflare Pages (`thepan` project).

GitHub Actions and CircleCI are not production deploy executors for this site. They must not be added as a required publish step.
