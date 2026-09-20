import { access, copyFile, cp, mkdir, readFile, rm } from 'node:fs/promises';
import { constants } from 'node:fs';
import { resolve } from 'node:path';

const root = resolve(import.meta.dirname, '..');
const output = resolve(root, 'dist');
const files = ['index.html', 'styles-v2.css', 'script.js', 'robots.txt', 'sitemap.xml'];
const directories = ['assets', 'onepiece'];

for (const file of files) {
  await access(resolve(root, file), constants.R_OK);
}
for (const directory of directories) {
  await access(resolve(root, directory), constants.R_OK);
}

const html = await readFile(resolve(root, 'index.html'), 'utf8');
const requiredText = [
  'THE PAN',
  'LATEST',
  'TRANSMISSION',
  'THREE',
  'DOORS',
  'prefers-reduced-motion'
];

const combined = `${html}\n${await readFile(resolve(root, 'styles-v2.css'), 'utf8')}`;
for (const text of requiredText) {
  if (!combined.includes(text)) throw new Error(`Missing required content: ${text}`);
}

await rm(output, { recursive: true, force: true });
await mkdir(output, { recursive: true });

for (const file of files) {
  await copyFile(resolve(root, file), resolve(output, file));
}
for (const directory of directories) {
  await cp(resolve(root, directory), resolve(output, directory), { recursive: true });
}

console.log(`Built THE PAN mock: ${files.length} files + ${directories.join(', ')} → dist/`);
