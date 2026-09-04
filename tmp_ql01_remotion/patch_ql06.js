const fs = require('fs');

const path = 'E:/remotion/src/ql-batch/page-config.ts';
let source = fs.readFileSync(path, 'utf8');
const marker = /"x": 250,\s*"y": 260,\s*"width": 1440,\s*"height": 600\s*}/;
const replacement = `"x": 250,
            "y": 260,
            "width": 1440,
            "height": 600
          },
          {
            "x": 1240,
            "y": 500,
            "width": 570,
            "height": 420
          }`;

if (!marker.test(source)) {
  throw new Error('QL-06 source rectangle not found');
}

source = source.replace(marker, replacement);
fs.writeFileSync(path, source, 'utf8');
