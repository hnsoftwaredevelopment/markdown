# HN Software Development Product Website Design

Date: 2026-07-09
Project: hnsoftwaredevelopment

## Goal

Build a public Blazor website for HN Software Development where visitors can read about the software products, view screenshots where available, download manuals and installers, and submit product-specific bug reports or feature requests.

The first version should stay practical and maintainable. The site is a product catalog and support entry point, not a large marketing platform.

## Public Products

The public software catalog contains these products:

- Saga
- Modelbouwer Dekbeplanking
- Modelbouwer Werkbank
- MySqlAnalyzer
- Amusing Android app

Saga and MySqlAnalyzer may be shown as in development. That status should be visible and honest, while still allowing users to understand what the applications are intended to do.

Amusing Beheer is not public and must not appear in the public navigation or public product catalog.

## Site Structure

The main navigation contains:

- Home
- Software
  - Saga
  - Modelbouwer Dekbeplanking
  - Modelbouwer Werkbank
  - MySqlAnalyzer
  - Amusing Android app
- Over mij

The header also contains a language selector using flag icons only. The visible selector should not use text labels such as "Nederlands", "English", or "Deutsch". The underlying HTML should still provide accessible labels for screen readers.

## Language Strategy

Dutch is the primary content language and should be the first complete version.

The site should be structured so English and German can be added later without redesigning the navigation or product pages. The product applications themselves may support more languages, but the website scope is Dutch, English, and German.

For the first implementation, it is acceptable to complete Dutch content first and prepare the UI structure for the other languages.

## Home Page

The home page introduces HN Software Development and gives visitors a direct path to the products.

It should contain:

- A short introduction to HN Software Development.
- A concise overview of the public products.
- Clear links to each product page.

The tone should be clear, modest, and useful. Avoid a heavy marketing landing page.

## Product Page Pattern

Every product page should follow a consistent pattern:

1. Product name and short summary.
2. Product status, when relevant.
3. Description of the target user and the problem the application solves.
4. Key features.
5. Screenshot section, prepared for one or more screenshots.
6. Downloads section.
7. Support actions for bug reports and feature requests.

The screenshot section may be empty or use a simple "screenshots will be added later" state until real screenshots are available.

## Downloads

Downloads should be prepared as files served by the website.

Use a structure such as:

```text
wwwroot/downloads/<product>/manuals/
wwwroot/downloads/<product>/installers/
wwwroot/downloads/<product>/screenshots/
```

Each product page should have prepared download slots for:

- Manual
- Application installer, archive, or APK where applicable

If a file is not available yet, the page should clearly show that the download is not yet available. The first version should not depend on GitHub Releases, because releases are not yet part of the current workflow.

The design should keep a future move to GitHub Releases possible without changing the public page layout.

## Support Flow

Each product page should provide two compact actions:

- Bug melden
- Feature request indienen

These actions should be available directly on the product page, not on a separate support page.

The form should collect:

- Product
- Request type: bug or feature request
- Title
- Description
- Optional version or platform
- Optional contact detail

Email contact should not be required. The public "Over mij" page should link to GitHub and LinkedIn, but should not publish an email address in the first version.

The website should later send support submissions to Cloudflare. Cloudflare then creates an issue in the correct GitHub repository. This follows the existing pattern already used by the Modelbouwer Dekbeplanking app.

## Cloudflare Integration Direction

The first implementation can include the UI and a clear boundary for the support submission API. The Cloudflare integration can be implemented as a separate step.

The intended flow is:

1. User submits bug report or feature request from a product page.
2. Blazor sends the submission to a Cloudflare endpoint.
3. Cloudflare validates the submission.
4. Cloudflare creates a GitHub issue in the product repository.
5. The website shows a success or failure message.

The endpoint should not expose GitHub tokens or secrets to the browser.

## About Page

The "Over mij" page should describe the person behind HN Software Development.

It should include:

- Personal background.
- Why these applications are made.
- Links to GitHub and LinkedIn.

Do not include a public email address in the first version.

## Visual Direction

The site should feel like a clear software product catalog:

- Professional and calm.
- Easy to scan.
- More practical than promotional.
- Good typography and spacing.
- Consistent product sections.
- No oversized marketing hero or decorative layout that distracts from the software.

Cards may be used for product summaries and repeated download/support blocks, but the site should avoid unnecessary nested cards.

## Implementation Notes

The existing project is a Blazor Web App targeting .NET 10. It already contains Razor pages for several products and a custom main layout with a header, software dropdown, and footer.

Recommended implementation direction:

- Keep product pages as normal Razor pages for now.
- Rename the public DeckPlanking page and labels to Modelbouwer Dekbeplanking.
- Rename the public WorkBench page and labels to Modelbouwer Werkbank.
- Add pages for MySqlAnalyzer and Amusing Android app.
- Add reusable styles and small components only where they reduce duplication, such as product status, downloads, screenshots, or support actions.
- Keep Amusing Beheer out of public routes and navigation.

## Testing And Review

Before considering the implementation complete:

- Build the Blazor project.
- Verify the home page, each product page, and the about page.
- Verify the language selector is visible as flags and has accessible labels.
- Verify missing downloads are handled clearly.
- Verify support actions are present per product.
- Verify Amusing Beheer is not present in public navigation.
- Check the layout on desktop and mobile widths.

