# Taylor Detailing

Marketing website for **Taylor Detailing**, an auto detailing business serving
Roanoke, Virginia and the surrounding area.

It's a single-page, fully responsive static site (HTML, CSS, vanilla JS) — no
build step required.

## Structure

```
index.html              # The page
assets/css/styles.css   # Styles (brand palette pulled from the logo)
assets/js/main.js       # Nav, scroll reveal, gallery lightbox
images/                 # Logo + cleaned-up vehicle photos
process_images.py       # Script used to clean up the original photos
```

## Running locally

Any static file server works, e.g.:

```bash
python -m http.server 5500
```

Then open <http://localhost:5500>.

## Photo cleanup

The original phone photos were rotated, oversized, and had distracting
backgrounds. `process_images.py` (Pillow) fixes EXIF orientation, crops out
background clutter, enhances brightness/contrast/color, and exports
web-optimized JPEGs into `images/`. The original source files are kept in the
repo root.

## To customize

- **Phone number:** replace the placeholder `(540) 555-0123` in `index.html`
  (search for `TODO`) and the matching `tel:` link.
- **Email:** the quote form and contact link use `benhart8202@gmail.com`.
- **Service area / hours / copy:** all editable directly in `index.html`.
- **Hosting:** drop the folder on any static host (GitHub Pages, Netlify,
  Cloudflare Pages, etc.).
