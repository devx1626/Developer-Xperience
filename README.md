# Developer Xperience - HTML & CSS Roadmap

Project created for **Dev** (Africa-based aspiring fullstack developer) to learn web development through structured roadmaps.

## Project Structure

```
/home/devx1626/Documents/dev/html/
│
├── index.html          # Main landing page with navigation to both roadmaps
├── html.html           # HTML Learning Roadmap (10 modules, 63 sections)
├── css.html            # CSS Learning Roadmap (10 modules, matching structure)
├── main.css            # Enhanced stylesheet (shared between html.html & css.html)
├── *.png               # Icon images (favicon sizes)
├── *.png               # Banner image (devx_banner.png)
├── site.webmanifest    # Web app manifest
└── *.html              # Additional HTML files (if needed)
```

## Roadmap Format

Both `html.html` and `css.html` follow the same consistent structure:

- **10 modules** (`module-group` class)
- **Submodule asides** (`submodule-aside` class) with nested links
- **Section IDs** in `module-X-Y` format (e.g., `#module-1-1`, `#module-5-37`)
- **Article cards** (`card` class) for each module
- **Shared stylesheet** (`main.css`) for consistent theming

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

The stylesheet was improved with:

- **Color palette**: 15 semantic variables (was 8) - `--bg-1`, `--bg-2`, `--bg-card`, `--border`, `--text`, `--text-muted`, `--accent`, etc.
- **Modular typography scale**: xs through 4xl in REM units
- **Shadow system**: 3 shadow levels (card, hover, focus) with depth
- **Border-radius system**: `--radius` (16px) and `--radius-sm` (8px)
- **3 responsive breakpoints**: 768px, 560px, and `prefers-reduced-motion`
- **Enhanced focus-visible**: Accent-colored outlines on all interactive elements
- **Table semantics**: Header backgrounds, proper spacing
- **Special elements**: pre/code/kbd styling

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

4. **Update `index.html`** if adding a new roadmap section:
   - Add new `<article class="card">` with module links
   - Follow the same format as existing CSS/HTML links

5. **Update `main.css`** if needing new styles:
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
- Images stored in project root: `devx_banner.png`, favicon files
- CSS link: `<link rel="stylesheet" href="main.css">`
- Manifest: `site.webmanifest`
- Follow the module-X-Y section ID convention for consistency
- Test responsiveness at 768px, 560px, and with reduced motion preferences
