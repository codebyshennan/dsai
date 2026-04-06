import { fileURLToPath } from 'node:url';
import fs from 'node:fs';
import path from 'node:path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

/** Default max items per slide before splitting into multiple sections */
const DEFAULT_CHUNK_SIZE = 10;

/** Use two columns when a chunk has at least this many items (unless columns overridden) */
const AUTO_COLUMN_MIN_ITEMS = 8;

/** Apply compact typography at or above this many items in one chunk */
const COMPACT_ITEM_THRESHOLD = 7;

/** Escape text for safe HTML insertion (trusted author content; still avoids breakage from & < >). */
function escapeHtml(s) {
    if (s == null) return '';
    return String(s)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;');
}

/**
 * Process inline markdown: `**bold**` → <strong>, `[text](url)` → <a>.
 * Non-link segments are HTML-escaped; link text and URLs are escaped individually.
 */
function formatInline(s) {
    if (s == null) return '';
    const str = String(s);
    const linkRe = /\[([^\]]+)\]\(([^)]+)\)/g;
    let result = '';
    let lastIndex = 0;
    let match;
    while ((match = linkRe.exec(str)) !== null) {
        // escape and bold-ify the plain text segment before this link
        result += applyBold(escapeHtml(str.slice(lastIndex, match.index)));
        result += `<a href="${escapeHtml(match[2])}" target="_blank" rel="noopener">${escapeHtml(match[1])}</a>`;
        lastIndex = linkRe.lastIndex;
    }
    result += applyBold(escapeHtml(str.slice(lastIndex)));
    return result;
}

function applyBold(s) {
    return s.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
}

function chunkArray(arr, size) {
    const chunks = [];
    for (let i = 0; i < arr.length; i += size) {
        chunks.push(arr.slice(i, i + size));
    }
    return chunks;
}

/** Sum of string lengths of items (rough density estimate) */
function itemsCharTotal(items) {
    return items.reduce((acc, x) => acc + String(x).length, 0);
}

/**
 * @param {string[]} items
 * @param {boolean} ordered
 * @param {number} [startAt] 1-based start for <ol>
 */
function renderList(items, ordered, startAt = 1) {
    const listType = ordered ? 'ol' : 'ul';
    const startAttr = ordered && startAt > 1 ? ` start="${startAt}"` : '';
    const lis = items.map((item) => `<li>${formatInline(item)}</li>`).join('\n');
    return `
                    <div class="list-container">
                        <${listType}${startAttr}>
                            ${lis}
                        </${listType}>
                    </div>
                `;
}

/**
 * Split items across N columns; for ordered lists, second+ columns use <ol start="…">.
 * @param {string[]} items
 * @param {boolean} ordered
 * @param {number} columns 2 or 3
 */
function renderListColumns(items, ordered, columns) {
    const n = Math.min(3, Math.max(2, columns));
    if (items.length < 6 || n < 2) {
        return renderList(items, ordered);
    }
    const per = Math.ceil(items.length / n);
    const parts = [];
    for (let c = 0; c < n; c++) {
        const slice = items.slice(c * per, (c + 1) * per);
        if (slice.length === 0) continue;
        const startAt = ordered ? c * per + 1 : 1;
        parts.push(renderList(slice, ordered, ordered ? startAt : 1));
    }
    const gridClass = n === 3 ? 'three-column' : 'two-column';
    return `
                    <div class="${gridClass}">
                        ${parts.join('\n')}
                    </div>
                `;
}

/**
 * @param {object} content - slide.content
 * @param {string[]} chunkItems
 */
function renderItemsHtml(content, chunkItems) {
    const ordered = Boolean(content.ordered);
    const explicitCols = content.columns;
    let columns = 1;
    if (explicitCols === 2 || explicitCols === 3) {
        columns = explicitCols;
    } else if (explicitCols == null && chunkItems.length >= AUTO_COLUMN_MIN_ITEMS) {
        columns = chunkItems.length >= 18 ? 3 : 2;
    }

    if (columns >= 2 && chunkItems.length >= 6) {
        return renderListColumns(chunkItems, ordered, columns);
    }
    return renderList(chunkItems, ordered);
}

/**
 * @returns {string} HTML for one or more <section> elements
 */
function generateContentSlideHtml(slide, index) {
    const content = slide.content;
    if (!content || typeof content !== 'object') {
        console.warn(`Slide ${index}: content slide missing "content" object, skipping`);
        return '';
    }

    const items = Array.isArray(content.items) ? content.items : [];
    const footerHtml = `<div class="slide-footer">Data Science &amp; Analytics | Skills Union</div>`;

    if (items.length === 0) {
        const boxTitle = content.title ? `<h3>${formatInline(content.title)}</h3>` : '';
        const slideTitle = formatInline(slide.title ?? '');
        return `
                <section>
                    <div class="content-wrapper">
                        <h2>${slideTitle}</h2>
                        <div class="box">
                            ${boxTitle}
                        </div>
                    </div>
                    ${footerHtml}
                </section>
            `;
    }

    let chunkSize = DEFAULT_CHUNK_SIZE;
    if (content.chunkSize === false || content.chunkSize === 0) {
        chunkSize = Infinity;
    } else if (typeof content.chunkSize === 'number' && content.chunkSize > 0) {
        chunkSize = content.chunkSize;
    }

    const chunks = chunkSize >= Infinity ? [items] : chunkArray(items, chunkSize);

    return chunks
        .map((chunkItems, partIdx) => {
            const partTotal = chunks.length;
            const titleBase = slide.title ?? '';
            const partSuffix = partTotal > 1 ? ` (${partIdx + 1}/${partTotal})` : '';
            const slideTitle = formatInline(titleBase + partSuffix);

            const boxTitle = content.title ? `<h3>${formatInline(content.title)}</h3>` : '';
            const itemsHtml = renderItemsHtml(content, chunkItems);

            const compact =
                chunkItems.length >= COMPACT_ITEM_THRESHOLD ||
                itemsCharTotal(chunkItems) > 520;
            const boxClass = compact ? 'box box--compact' : 'box';

            return `
                <section>
                    <div class="content-wrapper">
                        <h2>${slideTitle}</h2>
                        <div class="${boxClass}">
                            ${boxTitle}
                            ${itemsHtml}
                        </div>
                    </div>
                    ${footerHtml}
                </section>
            `;
        })
        .join('\n');
}

function generateSlideHtml(slide, index) {
    switch (slide.type) {
        case 'title': {
            const footerHtml = `<div class="slide-footer">Data Science &amp; AI | Skills Union &times; Localized</div>`;
            const title = formatInline(slide.title ?? '');
            const subtitle = formatInline(slide.subtitle ?? '');
            const subtitleBlock = subtitle
                ? `<h3>${subtitle}</h3>`
                : '';
            return `
                <section class="slide-title">
                    <div class="content-wrapper">
                        <h1>${title}</h1>
                        ${subtitleBlock}
                    </div>
                    ${footerHtml}
                </section>
            `;
        }
        case 'content':
            return generateContentSlideHtml(slide, index);
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
        .replaceAll('{{title}}', escapeHtml(data.title))
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
