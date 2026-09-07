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

## CSS Enhancements (`main.css`)

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
