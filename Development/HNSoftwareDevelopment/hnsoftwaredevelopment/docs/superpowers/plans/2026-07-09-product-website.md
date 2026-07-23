# Product Website Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** Build the first public HN Software Development product website in the existing Blazor project.

**Architecture:** Keep the current Blazor Web App structure and use normal Razor pages for product content. Add small reusable page sections only where they reduce repeated markup, while keeping product text easy to edit per page.

**Tech Stack:** .NET 10 Blazor Web App, Razor components, scoped/global CSS, static files under `wwwroot`.

---

## File Structure

- Modify `Components/Layout/MainLayout.razor`: update navigation labels, add product routes, add flag-only language selector.
- Modify `Program.cs`: enable interactive server rendering so product support actions can update local UI state.
- Modify `Components/App.razor`: set Dutch document language and render routes interactively.
- Modify `Components/Pages/Home.razor`: replace starter text with Dutch product catalog landing content.
- Modify `Components/Pages/About.razor`: turn starter text into an "Over mij" page with GitHub and LinkedIn links.
- Modify `Components/Pages/Saga.razor`: implement product page pattern.
- Rename and modify `Components/Pages/DeckPlanking.razor` to `Components/Pages/ModelbouwerDekbeplanking.razor`: implement product page pattern and keep an optional route alias.
- Rename and modify `Components/Pages/WorkBench.razor` to `Components/Pages/ModelbouwerWerkbank.razor`: implement product page pattern and keep an optional route alias.
- Create `Components/Pages/MySqlAnalyzer.razor`: implement product page pattern.
- Create `Components/Pages/AmusingAndroid.razor`: implement product page pattern.
- Create `Components/Shared/ProductStatus.razor`: render a compact product status label.
- Create `Components/Shared/DownloadPanel.razor`: render manual/application download slots with unavailable states.
- Create `Components/Shared/SupportActions.razor`: render compact bug and feature request UI controls wired to a local form state.
- Modify `wwwroot/app.css`: add calm product catalog layout styles, flag selector styles, responsive product grid, product page sections, downloads, and support actions.
- Create tracked download directories under `wwwroot/downloads/<product>/manuals`, `installers`, and `screenshots` using `.gitkeep` files.

## Task 1: Reusable Product Components

**Files:**
- Create: `Components/Shared/ProductStatus.razor`
- Create: `Components/Shared/DownloadPanel.razor`
- Create: `Components/Shared/SupportActions.razor`

- [x] **Step 1: Create `ProductStatus`**

```razor
@if (!string.IsNullOrWhiteSpace(Text))
{
    <span class="product-status @CssClass">@Text</span>
}

@code {
    [Parameter] public string? Text { get; set; }
    [Parameter] public string CssClass { get; set; } = "status-stable";
}
```

- [x] **Step 2: Create `DownloadPanel`**

```razor
<section class="product-section download-section" aria-labelledby="@HeadingId">
    <div class="section-heading">
        <h2 id="@HeadingId">Downloads</h2>
        <p>Handleiding en installatiebestanden komen hier beschikbaar zodra ze klaarstaan.</p>
    </div>

    <div class="download-grid">
        <div class="download-card">
            <h3>Handleiding</h3>
            <p>@ManualDescription</p>
            @if (!string.IsNullOrWhiteSpace(ManualHref))
            {
                <a class="button primary-button" href="@ManualHref" download>Handleiding downloaden</a>
            }
            else
            {
                <span class="button disabled-button" aria-disabled="true">Binnenkort beschikbaar</span>
            }
        </div>

        <div class="download-card">
            <h3>@ApplicationTitle</h3>
            <p>@ApplicationDescription</p>
            @if (!string.IsNullOrWhiteSpace(ApplicationHref))
            {
                <a class="button primary-button" href="@ApplicationHref" download>Applicatie downloaden</a>
            }
            else
            {
                <span class="button disabled-button" aria-disabled="true">Binnenkort beschikbaar</span>
            }
        </div>
    </div>
</section>

@code {
    private string HeadingId => $"{ProductSlug}-downloads";

    [Parameter, EditorRequired] public string ProductSlug { get; set; } = string.Empty;
    [Parameter] public string? ManualHref { get; set; }
    [Parameter] public string? ApplicationHref { get; set; }
    [Parameter] public string ManualDescription { get; set; } = "De handleiding is nog niet gepubliceerd.";
    [Parameter] public string ApplicationTitle { get; set; } = "Applicatie";
    [Parameter] public string ApplicationDescription { get; set; } = "Het installatiebestand is nog niet gepubliceerd.";
}
```

- [x] **Step 3: Create `SupportActions`**

```razor
<section class="product-section support-section" aria-labelledby="@HeadingId">
    <div class="section-heading">
        <h2 id="@HeadingId">Bug melden of idee voorstellen</h2>
        <p>Gebruik deze ingang straks om direct een melding voor @ProductName door te geven.</p>
    </div>

    <div class="support-actions" role="group" aria-label="Supporttype kiezen">
        <button type="button" class="button secondary-button @(SelectedType == "Bug" ? "selected" : null)" @onclick='() => SelectType("Bug")'>Bug melden</button>
        <button type="button" class="button secondary-button @(SelectedType == "Feature request" ? "selected" : null)" @onclick='() => SelectType("Feature request")'>Feature request indienen</button>
    </div>

    <EditForm Model="this" OnSubmit="HandleSubmit" class="support-form">
        <div class="form-row">
            <label for="@TitleId">Titel</label>
            <input id="@TitleId" @bind="Title" placeholder="Korte samenvatting" />
        </div>
        <div class="form-row">
            <label for="@DescriptionId">Beschrijving</label>
            <textarea id="@DescriptionId" @bind="Description" rows="4" placeholder="Beschrijf wat er gebeurt of wat je graag zou willen zien"></textarea>
        </div>
        <div class="form-row two-columns">
            <div>
                <label for="@VersionId">Versie of platform</label>
                <input id="@VersionId" @bind="VersionOrPlatform" placeholder="Optioneel" />
            </div>
            <div>
                <label for="@ContactId">Contact</label>
                <input id="@ContactId" @bind="Contact" placeholder="Optioneel" />
            </div>
        </div>
        <button type="submit" class="button primary-button">Voorbereiden</button>
        @if (!string.IsNullOrWhiteSpace(Message))
        {
            <p class="form-message">@Message</p>
        }
    </EditForm>
</section>

@code {
    private string HeadingId => $"{ProductSlug}-support";
    private string TitleId => $"{ProductSlug}-support-title";
    private string DescriptionId => $"{ProductSlug}-support-description";
    private string VersionId => $"{ProductSlug}-support-version";
    private string ContactId => $"{ProductSlug}-support-contact";

    private string SelectedType { get; set; } = "Bug";
    private string? Title { get; set; }
    private string? Description { get; set; }
    private string? VersionOrPlatform { get; set; }
    private string? Contact { get; set; }
    private string? Message { get; set; }

    [Parameter, EditorRequired] public string ProductName { get; set; } = string.Empty;
    [Parameter, EditorRequired] public string ProductSlug { get; set; } = string.Empty;

    private void SelectType(string type)
    {
        SelectedType = type;
        Message = null;
    }

    private void HandleSubmit()
    {
        Message = $"De {SelectedType.ToLowerInvariant()} voor {ProductName} is lokaal voorbereid. De Cloudflare-koppeling wordt in een volgende stap aangesloten.";
    }
}
```

- [x] **Step 4: Build**

Run: `dotnet build`
Expected: build succeeds.

## Task 2: Navigation And Site Shell

**Files:**
- Modify: `Components/Layout/MainLayout.razor`
- Modify: `Program.cs`
- Modify: `Components/App.razor`

- [x] **Step 1: Update navigation and language selector**

Use these route labels:

```razor
<li><NavLink href="software/saga">Saga</NavLink></li>
<li><NavLink href="software/modelbouwer-dekbeplanking">Modelbouwer Dekbeplanking</NavLink></li>
<li><NavLink href="software/modelbouwer-werkbank">Modelbouwer Werkbank</NavLink></li>
<li><NavLink href="software/mysqlanalyzer">MySqlAnalyzer</NavLink></li>
<li><NavLink href="software/amusing-android">Amusing Android app</NavLink></li>
```

Add flag-only links/buttons with accessible labels:

```razor
<div class="language-selector" aria-label="Taalkeuze">
    <a href="/" aria-label="Nederlands" class="flag-link active" lang="nl">🇳🇱</a>
    <a href="/" aria-label="English" class="flag-link" lang="en">🇬🇧</a>
    <a href="/" aria-label="Deutsch" class="flag-link" lang="de">🇩🇪</a>
</div>
```

- [x] **Step 2: Enable interactive server rendering**

Change Razor component registration in `Program.cs` to:

```csharp
builder.Services.AddRazorComponents()
    .AddInteractiveServerComponents();
```

Change component mapping in `Program.cs` to:

```csharp
app.MapRazorComponents<App>()
    .AddInteractiveServerRenderMode();
```

- [x] **Step 3: Set default document language and route render mode**

Change `Components/App.razor` from `html lang="en"` to:

```html
<html lang="nl">
```

Render routes interactively:

```razor
<Routes @rendermode="InteractiveServer" />
```

- [x] **Step 4: Build**

Run: `dotnet build`
Expected: build succeeds.

## Task 3: Product Pages

**Files:**
- Modify: `Components/Pages/Saga.razor`
- Rename and modify: `Components/Pages/DeckPlanking.razor` to `Components/Pages/ModelbouwerDekbeplanking.razor`
- Rename and modify: `Components/Pages/WorkBench.razor` to `Components/Pages/ModelbouwerWerkbank.razor`
- Create: `Components/Pages/MySqlAnalyzer.razor`
- Create: `Components/Pages/AmusingAndroid.razor`

- [x] **Step 1: Implement each product page with this structure**

Each page should include:

```razor
<section class="product-hero">
    <div>
        <h1>Productnaam</h1>
        <p class="product-summary">Korte Nederlandse samenvatting.</p>
    </div>
    <ProductStatus Text="In ontwikkeling" CssClass="status-development" />
</section>

<section class="product-section">
    <h2>Voor wie is dit?</h2>
    <p>Doelgroep en probleem.</p>
</section>

<section class="product-section">
    <h2>Belangrijkste mogelijkheden</h2>
    <ul class="feature-list">
        <li>Concrete mogelijkheid.</li>
    </ul>
</section>

<section class="product-section screenshot-section">
    <h2>Screenshots</h2>
    <p class="empty-state">Screenshots worden toegevoegd zodra ze beschikbaar zijn.</p>
</section>

<DownloadPanel ProductSlug="product-slug" />
<SupportActions ProductName="Productnaam" ProductSlug="product-slug" />
```

- [x] **Step 2: Preserve route aliases for renamed pages**

For Modelbouwer Dekbeplanking:

```razor
@page "/software/modelbouwer-dekbeplanking"
@page "/software/deckplanking"
```

For Modelbouwer Werkbank:

```razor
@page "/software/modelbouwer-werkbank"
@page "/software/workbench"
```

- [x] **Step 3: Build**

Run: `dotnet build`
Expected: build succeeds.

## Task 4: Home And About Pages

**Files:**
- Modify: `Components/Pages/Home.razor`
- Modify: `Components/Pages/About.razor`

- [x] **Step 1: Replace home page starter text**

Add Dutch introduction and a product grid linking to all public product pages. Do not include Amusing Beheer.

- [x] **Step 2: Replace about page starter text**

Add Dutch background text and links:

```razor
<a href="https://github.com/hnsoftwaredevelopment" rel="noopener noreferrer" target="_blank">GitHub</a>
<a href="https://www.linkedin.com/" rel="noopener noreferrer" target="_blank">LinkedIn</a>
```

Use `https://github.com/hnsoftwaredevelopment` for GitHub. Use `https://www.linkedin.com/` as the current LinkedIn destination until the exact public profile URL is supplied.

- [x] **Step 3: Build**

Run: `dotnet build`
Expected: build succeeds.

## Task 5: Styling And Static Download Structure

**Files:**
- Modify: `wwwroot/app.css`
- Create: `.gitkeep` files under `wwwroot/downloads/...`

- [x] **Step 1: Add CSS for site catalog**

Add styles for:

- header language selector
- product grid
- product hero
- product status
- product sections
- download cards
- support form
- responsive layout

- [x] **Step 2: Create static directories**

Create these tracked empty-directory markers:

```text
wwwroot/downloads/saga/manuals/.gitkeep
wwwroot/downloads/saga/installers/.gitkeep
wwwroot/downloads/saga/screenshots/.gitkeep
wwwroot/downloads/modelbouwer-dekbeplanking/manuals/.gitkeep
wwwroot/downloads/modelbouwer-dekbeplanking/installers/.gitkeep
wwwroot/downloads/modelbouwer-dekbeplanking/screenshots/.gitkeep
wwwroot/downloads/modelbouwer-werkbank/manuals/.gitkeep
wwwroot/downloads/modelbouwer-werkbank/installers/.gitkeep
wwwroot/downloads/modelbouwer-werkbank/screenshots/.gitkeep
wwwroot/downloads/mysqlanalyzer/manuals/.gitkeep
wwwroot/downloads/mysqlanalyzer/installers/.gitkeep
wwwroot/downloads/mysqlanalyzer/screenshots/.gitkeep
wwwroot/downloads/amusing-android/manuals/.gitkeep
wwwroot/downloads/amusing-android/installers/.gitkeep
wwwroot/downloads/amusing-android/screenshots/.gitkeep
```

- [x] **Step 3: Build**

Run: `dotnet build`
Expected: build succeeds.

## Task 6: Verification

**Files:**
- Verify: all changed Blazor files

- [x] **Step 1: Run build**

Run: `dotnet build`
Expected: build succeeds with no errors.

- [x] **Step 2: Verify content by search**

Run:

```powershell
rg -n "Amusing Beheer|DeckPlanking|WorkBench" Components wwwroot
```

Expected:

- No public navigation label for Amusing Beheer.
- No visible public labels `DeckPlanking` or `WorkBench`.
- Old route aliases may remain only in `@page` directives.

- [x] **Step 3: Run the app**

Run:

```powershell
dotnet run --urls http://localhost:5206
```

Open `http://localhost:5206` and verify:

- Home page shows all five public products.
- Software menu links to all five public product pages.
- Flag selector is visible as flags.
- Every product page has downloads and support actions.
- About page has GitHub and LinkedIn links and no email address.
