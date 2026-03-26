import { fileURLToPath } from 'node:url';
import fs from 'node:fs';
import path from 'node:path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

/** Escape text for safe HTML insertion (trusted author content; still avoids breakage from & < >). */
function escapeHtml(s) {
    if (s == null) return '';
    return String(s)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;');
}

/** After escaping, turn `**segment**` into <strong> (same convention as course markdown notes). */
function formatInline(s) {
    return escapeHtml(s).replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
}

function generateSlideHtml(slide, index) {
    const footerHtml = `<div class="slide-footer">Data Science &amp; Analytics | Skills Union</div>`;
    switch (slide.type) {
        case 'title': {
            const title = formatInline(slide.title ?? '');
            const subtitle = formatInline(slide.subtitle ?? '');
            const subtitleBlock = subtitle
                ? `<h3>${subtitle}</h3>`
                : '';
            return `
                <section>
                    <div class="content-wrapper">
                        <h1>${title}</h1>
                        ${subtitleBlock}
                    </div>
                    ${footerHtml}
                </section>
            `;
        }
        case 'content': {
            const content = slide.content;
            if (!content || typeof content !== 'object') {
                console.warn(`Slide ${index}: content slide missing "content" object, skipping`);
                return '';
            }
            let itemsHtml = '';

            if (Array.isArray(content.items)) {
                const listType = content.ordered ? 'ol' : 'ul';
                const lis = content.items.map((item) => `<li>${formatInline(item)}</li>`).join('\n');
                itemsHtml = `
                    <div class="list-container">
                        <${listType}>
                            ${lis}
                        </${listType}>
                    </div>
                `;
            }

            const boxTitle = content.title ? `<h3>${formatInline(content.title)}</h3>` : '';
            const slideTitle = formatInline(slide.title ?? '');

            return `
                <section>
                    <div class="content-wrapper">
                        <h2>${slideTitle}</h2>
                        <div class="box">
                            ${boxTitle}
                            ${itemsHtml}
                        </div>
                    </div>
                    ${footerHtml}
                </section>
            `;
        }
        default:
            console.warn(`Slide ${index}: unknown type "${slide.type}", skipping`);
            return '';
    }
}

function buildSlides(moduleDir) {
    const templatePath = path.join(__dirname, 'template.html');
    const dataPath = path.join(moduleDir, 'slides', 'data.json');
    const outputPath = path.join(moduleDir, 'slides', 'index.html');

    const slidesDir = path.dirname(outputPath);
    if (!fs.existsSync(slidesDir)) {
        fs.mkdirSync(slidesDir, { recursive: true });
    }

    if (!fs.existsSync(dataPath)) {
        console.error(`No slides data: ${dataPath}`);
        process.exit(1);
    }

    let template;
    let data;
    try {
        template = fs.readFileSync(templatePath, 'utf8');
        data = JSON.parse(fs.readFileSync(dataPath, 'utf8'));
    } catch (err) {
        console.error(err instanceof Error ? err.message : err);
        process.exit(1);
    }

    if (!data.title || !Array.isArray(data.slides)) {
        console.error('data.json must include "title" (string) and "slides" (array)');
        process.exit(1);
    }

    const slidesHtml = data.slides.map((s, i) => generateSlideHtml(s, i)).join('\n');

    const output = template
        .replace('{{title}}', escapeHtml(data.title))
        .replace('{{content}}', slidesHtml);

    fs.writeFileSync(outputPath, output);
    console.log(`Slides built successfully: ${outputPath}`);
}

const moduleDir = process.argv[2];
if (!moduleDir) {
    console.error('Usage: node slides/build.js <module-directory-relative-to-cwd>');
    console.error('Example: node slides/build.js 1-data-fundamentals/1.2-intro-python');
    process.exit(1);
}

buildSlides(path.resolve(process.cwd(), moduleDir));
