# Senflow AI Website

A modern, user-focused website for Senflow AI, dedicated to delivering practical, reliable, and user-friendly AI-powered applications.

## Features
- Responsive, modern design
- Dark and light theme support
- Multi-page layout: Home, Products, About
- Custom branding and logo
- Animated UI and interactive effects
- Clean, maintainable codebase

## Directory Structure
```
senflow-site/
├── static/
│   ├── css/
│   ├── images/
│   └── js/
├── templates/
├── index.html
├── products.html
├── about.html
├── README.md
└── ...
```

## Deployment
This project is primarily hosted as a static website using the **gh-pages** branch on GitHub Pages.

To deploy or update:
1. Make changes on the `main` branch.
2. Merge or sync `main` to `gh-pages` branch.
3. Push `gh-pages` to GitHub. GitHub Pages will serve the latest static content from `gh-pages`.

## Local Development
You can preview the site locally with any static file server, for example:

```bash
python -m http.server 8000
# or
npx serve
```
Then open [http://localhost:8000](http://localhost:8000) in your browser.

## Contributing
Pull requests and issues are welcome! Please fork the repo and submit your suggestions or bug reports.

## License
All rights reserved. © 2025 Senflow AI LLC 