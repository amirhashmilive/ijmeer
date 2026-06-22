const fs = require('fs');
const path = require('path');
const glob = require('glob');
const sizeOf = require('image-size');
const cheerio = require('cheerio');

const workspacePath = path.resolve(__dirname, '../../');

const files = glob.sync('**/*.html', { cwd: workspacePath, ignore: ['scratch/**', 'node_modules/**', '.git/**'] });

files.forEach(file => {
    const filePath = path.join(workspacePath, file);
    let content = fs.readFileSync(filePath, 'utf8');
    let modified = false;

    // Use regex to find img tags to ensure we don't rewrite the whole document
    const imgRegex = /<img\s+[^>]*>/gi;
    
    content = content.replace(imgRegex, (match) => {
        const isSelfClosing = match.trim().endsWith('/>');
        const $ = cheerio.load(match, null, false);
        const img = $('img');
        if (!img.length) return match;

        let changed = false;

        // 1. Check alt
        let alt = img.attr('alt');
        if (alt === undefined || alt.trim() === '') {
            let src = img.attr('src');
            if (src) {
                let cleanSrc = src.split('?')[0].split('#')[0];
                let filename = path.basename(cleanSrc, path.extname(cleanSrc));
                // Convert filename to Title Case
                let autoAlt = filename.replace(/[-_]/g, ' ').replace(/([a-z])([A-Z])/g, '$1 $2').trim();
                autoAlt = autoAlt.split(' ').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ');
                img.attr('alt', autoAlt || 'Image');
                changed = true;
            } else {
                img.attr('alt', 'Image');
                changed = true;
            }
        }

        // 2. Check width and height
        let hasWidth = img.attr('width') !== undefined;
        let hasHeight = img.attr('height') !== undefined;

        if (!hasWidth || !hasHeight) {
            let src = img.attr('src');
            if (src) {
                try {
                    let cleanSrc = src.split('?')[0].split('#')[0];
                    let tryPath1 = path.resolve(path.dirname(filePath), cleanSrc);
                    let tryPath2 = path.join(workspacePath, cleanSrc.startsWith('/') ? cleanSrc.substring(1) : cleanSrc);
                    
                    let actualPath = fs.existsSync(tryPath1) ? tryPath1 : (fs.existsSync(tryPath2) ? tryPath2 : null);

                    if (actualPath) {
                        const dimensions = sizeOf(actualPath);
                        if (!hasWidth && dimensions.width) {
                            img.attr('width', dimensions.width);
                            changed = true;
                        }
                        if (!hasHeight && dimensions.height) {
                            img.attr('height', dimensions.height);
                            changed = true;
                        }
                    } else {
                        console.warn(`Could not find image file for src: ${src} in ${file}`);
                    }
                } catch (e) {
                    console.error(`Error reading dimensions for src: ${src} in ${file}:`, e.message);
                }
            }
        }

        if (changed) {
            modified = true;
            let newTag = $.html('img');
            newTag = newTag.replace(/<\/img>$/i, '');
            // Restore self-closing if it was there
            if (isSelfClosing && !newTag.endsWith('/>')) {
                newTag = newTag.replace(/>$/, ' />');
            }
            return newTag;
        }

        return match;
    });

    if (modified) {
        fs.writeFileSync(filePath, content, 'utf8');
        console.log(`Updated ${file}`);
    }
});
console.log('Done');
