# Developer Xperience - HTML & CSS Roadmap

Project created for **Dev** (Africa-based aspiring fullstack developer) to learn web development through structured roadmaps.

## Project Structure

```
/
├── src/                # Eleventy templates - the source of truth for pages
│   ├── index.njk       # Landing page template
│   ├── html.njk        # HTML roadmap template
│   ├── css.njk         # CSS roadmap template
│   └── _includes/      # Shared partials (the DRY parts)
│       ├── head.njk    # <head> markup: favicons, meta, stylesheet, script
│       ├── banner.njk  # Banner: image, h1, and the more-options dropdown
│       ├── footer.njk  # Footer markup + footer navigation
│       ├── nav-index.njk # Landing-page dropdown menu
│       └── nav-course.njk # Course dropdown, rendered from front-matter data
├── assets/             # Static assets referenced by the generated pages
│   ├── css/
│   │   └── style.css   # Shared stylesheet
│   ├── js/
│   │   └── script.js   # Dropdown menu, module search, contact form behavior
│   ├── images/         # Banner, logo, and the "more options" SVG icon
│   └── icons/          # Favicons, apple-touch-icon, Android chrome icons
├── index.html          # GENERATED landing page (run `npm run build`)
├── html.html           # GENERATED HTML Learning Roadmap (10 modules)
├── css.html            # GENERATED CSS Learning Roadmap (10 modules, matching structure)
├── site.webmanifest    # Web app manifest
└── .eleventy.js        # Eleventy config: templates from src/, output to root
```

## Building the Site

The HTML pages are generated from the templates in `src/` by Eleventy, so shared markup (the `<head>`, banner, dropdown, and footer) is defined once in `src/_includes/` and reused by every page.

```bash
npm install        # first time only
npm run build      # regenerate index.html, html.html, css.html at the project root
npm start          # live-reload dev server at http://localhost:8080
```

Edit the templates in `src/`, then run `npm run build` - the finished pages appear at the project root, ready to open or deploy.

The course dropdown menus are **data-driven**: each roadmap template defines a
`modules:` list in its front matter (module ids, labels, and section anchors),
and `src/_includes/nav-course.njk` renders it. To add or reorder sections, edit
the front-matter list at the top of `src/html.njk` or `src/css.njk` - the menu
and the content stay in sync because every `title` maps to a real `id`.

### Canonical URLs and social cards

`src/_includes/head.njk` accepts a `canonical` front-matter value and builds
Open Graph/Twitter tags from it. For absolute URLs (recommended for social
previews), set the `SITE_URL` environment variable when building:

```bash
SITE_URL=https://your-domain.example npm run build
```

## Roadmap Format

Both `html.html` and `css.html` follow the same consistent structure:

- **10 modules** (`module-group` class)
- **Submodule asides** (`submodule-aside` class) with nested links
- **Section IDs** in `module-X-Y` format (e.g., `#module-1-1`, `#module-5-37`)
- **Article cards** (`card` class) for each module
- **Shared stylesheet** (`style.css`) for consistent theming

### Section ID Convention

``` 
module-1-1 through module-1-7   (Module 1: 7 sections)
module-2-1 through module-2-6   (Module 2: 6 sections)
module-3-1 through module-3-2   (Module 3: 2 sections)
module-4-1 through module-4-10  (Module 4: 10 sections)
module-5-1 through module-5-37  (Module 5: 37 sections - most complex)
module-6-1 through module-6-6   (Module 6: 6 sections)
module-7-1 through module-7-6   (Module 7: 6 sections)
module-8-1 through module-8-6   (Module 8: 6 sections)
module-9-1 through module-9-6   (Module 9: 6 sections)
module-10-1 through module-10-6 (Module 10: 6 sections)
```

**Total: 63 sections across 10 modules**

### CSS Roadmap Module Overview

The CSS roadmap follows the same 10-module structure as the HTML roadmap, covering:

- **Module 1: CSS Fundamentals** - Introduction, syntax, selectors, box model, colors/backgrounds, typography, links/navigation
- **Module 2: CSS Layout** - Positioning, Flexbox, CSS Grid, responsive design, media queries
- **Module 3: CSS Interactivity** - Pseudo-classes/pseudo-elements, transitions/animations, transforms, forms styling, focus states
- **Module 4: Advanced Layout Techniques** - CSS variables, calc/math functions, subgrid, gap/spacing, column balance
- **Module 5: Design Systems** - Responsive design patterns, mobile-first approach, cross-browser compatibility, accessibility, performance optimization
- **Module 6: Practical Projects** - Landing page, form, newsletter subscription
- **Module 7: CSS Architecture** - BEM methodology, scalable patterns, CSS organization, preprocessors, modern workflow
- **Module 8: CSS Grid Deep Dive** - Explicit vs implicit grid, named lines, auto-placement, subgrid details, accessibility
- **Module 9: Flexbox Mastery** - Main axis vs cross axis, alignment/justification, order property, nested flexbox, debugging
- **Module 10: Final Projects & Review** - Complete web page redesign, CSS portfolio layout, responsive admin dashboard, accessible component library, final exam project

### HTML Roadmap Module Overview

The HTML roadmap covers fundamentals through semantic elements:

- **Module 1: Introduction to HTML** - Markup languages, frontend development, HTML basics, semantics, CSS/JS introduction
- **Module 2: How the Web Works** - HTTP, domain name, hosting, DNS, browsers, SEO/GEO
- **Module 3: Your First HTML File** - HTML skeleton, saving files, browser viewing
- **Module 4: HTML Document Structure** - DOCTYPE, meta tags, semantic structure, code samples
- **Module 5: HTML Text Elements** - Headings, paragraphs, formatting, lines/breaks, summary table
- **Module 6: HTML Links** - Anchor elements, URLs, link targets, named anchors, accessible text
- **Module 7: HTML Images and Media** - Images, figure/captions, SVG, video/audio
- **Module 8: HTML Tables** - Table elements, rows/cells, headers, accessible tables
- **Module 9: HTML Forms** - Form elements, inputs, label association, controls/validation
- **Module 10: HTML5 Semantic Elements** - Landmarks, when not to use semantic elements, summary

The stylesheet (`style.css`) provides:

- **CSS custom properties**: `--bg`, `--card`, `--border`, `--accent`, `--accent-hover`, `--text`, `--code-bg`, `--code-text`
- **Fluid base typography**: `clamp()` on `html` scales text with the viewport
- **Responsive breakpoints**: 768px and 600px - banner, cards, and tables adapt to screen size (content stays single-column and full-width at every size)
- **Base reset**: `box-sizing: border-box` plus a margin/padding reset on every element, and a fixed multi-radial-gradient background on `body`
- **Accessibility**: visible `:focus-visible` outlines, a skip link (`.content-link`), `user-invalid` form styling, and a `prefers-reduced-motion` block
- **Dropdown menu**: "more options" popup navigation with Escape/outside-click/focus-out to close, plus Arrow key cycling between links
- **Styled tables**: summary tables with accent headers and zebra striping
- **Native CSS nesting**: no preprocessor required
- **Contact form**: HTML5 validation plus a JavaScript confirmation message (no backend)

## Adding New Content

### When adding new modules/sections:

1. **Update section IDs** following `module-X-Y` format
   - X = module number (1-10)
   - Y = section number within that module
   - Maintain consistent numbering within each module

2. **Update navigation** in the module-group/ul:
   ```html
   <li class="module-group">
     <a href="#moduleX">Module X: Title</a>
     <aside class="submodule-aside" aria-label="Module X submodules">
       <ul>
         <li><a href="#module-X-1">Section 1 Title</a></li>
         <!-- add more sections -->
       </ul>
     </aside>
   </li>
   ```

3. **Add content sections** with matching `id="module-X-Y"` attributes

4. **Update `src/index.njk`** if adding a new roadmap section:
   - Add new `<article class="card">` with module links
   - Follow the same format as existing CSS/HTML links

5. **Update `style.css`** if needing new styles:
   - Add to the `:root` variables section
   - Add media queries for new breakpoints
   - Maintain the existing shadow/typography scale

## User Profile

- **Name**: Dev (prefers 'Dev')
- **Role**: Aspiring fullstack developer
- **Location**: Africa/Accra timezone
- **Context**: Developing HTML projects in `Documents/dev/html`
- **Goal**: Progress from HTML fundamentals to fullstack development

## Related Projects

- `roadmap.sh/html` - Source curriculum for HTML roadmap
- `roadmap.sh/css` - Source curriculum for CSS roadmap (referenced for content)

## Development Notes

- All HTML files use UTF-8 encoding
- Images and icons live in `assets/images/` and `assets/icons/`, the stylesheet in `assets/css/`, and scripts in `assets/js/`
- CSS link: `<link rel="stylesheet" href="assets/css/style.css">` (added by `src/_includes/head.njk`)
- Manifest: `site.webmanifest`
- Pages are generated with Eleventy - edit `src/`, never the root `.html` files directly
- Follow the module-X-Y section ID convention for consistency
- Test responsiveness at 768px, 560px, and with reduced motion preferences
