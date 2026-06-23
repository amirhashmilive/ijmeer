const fs = require('fs');
const glob = require('glob');
const cheerio = require('cheerio');
const files = glob.sync('**/*.html', { cwd: '../../', ignore: ['scratch/**', 'node_modules/**', '.git/**'] });
let missingCount = 0;
files.forEach(f => {
  const content = fs.readFileSync('../../' + f, 'utf8');
  const $ = cheerio.load(content);
  $('img').each((i, el) => {
    const alt = $(el).attr('alt');
    const w = $(el).attr('width');
    const h = $(el).attr('height');
    if (alt === undefined || alt.trim() === '' || w === undefined || h === undefined) {
      console.log('Missing in', f, ':', $.html(el));
      missingCount++;
    }
  });
});
console.log('Images missing attributes:', missingCount);
