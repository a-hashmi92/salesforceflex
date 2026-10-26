# Salesforce Flex project page starter

Static HTML/CSS starter for GitHub Pages. No build process is required.

## Files
- `projects.html` — project overview page
- `projects/docusign-gen-automation.html` — first example project page
- `project-template.html` — reusable page template for future projects
- `styles.css` — shared responsive styling
- `downloads/` — put your case study PDFs here
- `assets/` — keep your logo here

## Before publishing
1. Copy `logo_transparent_background.png` into `assets/`.
2. Upload the DocuSign Gen PDF as `downloads/docusign-gen-case-study.pdf`, or update the PDF links to match your filename.
3. Verify the example page content and metric against your source document before publishing. Replace placeholder wording with accurate, approved details.
4. Upload the files/folders to the root of your existing GitHub Pages repository, preserving the folder structure.
5. Add a link to `projects.html` from your main site's navigation or project section.

## Add another project
1. Copy `project-template.html` to `projects/your-project-name.html`.
2. In the copied file, change the stylesheet path to `../styles.css` and image paths to `../assets/...`.
3. Put the PDF in `downloads/` and link to it using `../downloads/your-case-study.pdf`.
4. Add a project card to `projects.html` pointing to `projects/your-project-name.html`.

The download button works once you upload the PDF at the matching path. The PDF is not included in this starter package.
