// Offline SVG-to-PNG proof using the preinstalled Sharp/libvips renderer.
// This is not browser automation and does not use any network service.
const fs = require('node:fs');
const path = require('node:path');
const sharp = require('C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/sharp');
const source = path.resolve(__dirname, '../../skills-v2.7-development-snapshot-20260814/项目源码');
(async () => {
  for (const filename of fs.readdirSync(source).filter(name => name.endsWith('.drawio.svg'))) {
    const target = filename.includes('完整') ? 'diagram-business-flow.png' : 'diagram-project-overview.png';
    const result = await sharp(path.join(source, filename)).png().toFile(path.join(__dirname, target));
    console.log(`${target}: ${result.width} x ${result.height}`);
  }
  console.log(`Offline renderer: sharp ${sharp.versions.sharp}; librsvg ${sharp.versions.rsvg}`);
})().catch(error => { console.error(error); process.exitCode = 1; });
