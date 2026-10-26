# E01 Foundation

Set up the solution, build, logging and localization so all later stories build on the same base.

## US-0101 Solution and empty extension

**Status:** Done (accepted 2026-10-26)

As a developer, I want a solution that builds a VSIX which installs in Visual Studio 2026, so that every following story has a working base.

**Acceptance criteria**

- [x] Solution `ObjectExplorerForMySql.slnx` with projects Core (`netstandard2.0`), Vsix (`net48`), Core.Tests (`net10.0`).
- [x] VSIX manifest: name "Object Explorer for MySQL", installation target `[18.0,)` (amd64 and arm64), publisher hnsoftwaredevelopment, MIT license included.
- [x] F5 starts the Experimental Instance with the extension loaded. *(manual test)*
- [x] Menu item *View > Object Explorer for MySQL* opens an empty, dockable tool window. *(manual test)*
- [x] `.gitignore`, `.gitattributes`, `.editorconfig`, `Directory.Build.props` (nullable, latest C# version, warnings as errors in Core and tests), `global.json` (.NET 10 SDK, Microsoft.Testing.Platform).

**Tasks**

- [x] T-0101-01 Create solution and projects, `Directory.Build.props`, `.editorconfig`, `global.json`
- [x] T-0101-02 VSIX manifest and VSSDK-compatible VisualStudio.Extensibility setup
- [x] T-0101-03 Tool window (`ToolWindowPane`, WPF) and View menu command
- [x] T-0101-04 Test project with first tests (`ProductInfo.IsSupportedServerVersion`, 13 cases, all green)

**Implementation notes**

- The View menu command is placed in the same group as Server Explorer and SQL Server Object Explorer (`guidSHLMainMenu` / `IDG_VS_VIEW_DEV_WINDOWS`).
- The tool window opens as a tab next to Solution Explorer the first time. After that Visual Studio remembers the position you choose.
- Tool window colors come from `EnvironmentColors`, so it follows the Light, Dark and Blue themes.
- Building the VSIX needs Visual Studio's MSBuild (`dotnet build` cannot build the VSIX project). `dotnet test` works for the test project.
- Do not add `Microsoft.VSSDK.BuildTools` explicitly. `Microsoft.VisualStudio.Extensibility.Build` brings a compatible version (17.14.x). An explicit 18.9.820 reference caused error VSSDK1031 ("Extension could not be found") when deploying to the Experimental Instance.
- `UseCodebase` must stay `true` in the VSIX project. Without it the pkgdef has no `CodeBase` entry, Visual Studio looks for the package assembly in its own IDE folders and shows "The 'ObjectExplorerPackage' package did not load correctly" (FileNotFoundException in ActivityLog.xml).

**Manual test**

1. Open `ObjectExplorerForMySql.slnx` in Visual Studio 2026. Set `ObjectExplorerForMySql.Vsix` as startup project.
2. Press F5. Expected: the Experimental Instance starts without an error dialog about the extension.
3. Open *View*. Expected: "Object Explorer for MySQL" with a database icon, in the group with Server Explorer and SQL Server Object Explorer.
4. Click it. Expected: a tool window "Object Explorer for MySQL" opens as a tab next to Solution Explorer, with the text "No MySQL servers yet. ...".
5. Drag the tab to another dock position, close the window, open it again via *View*. Expected: it opens at the new position.
6. Switch theme (*Tools > Options > Environment > Visual Experience*) between Light and Dark. Expected: background and text color follow the theme.
7. *Extensions > Manage Extensions > Installed*: expected "Object Explorer for MySQL" 0.1.0 by hnsoftwaredevelopment.

**Test result**

2026-10-26, Herbert: accepted. The empty explorer opens from the View menu. Two build/load issues found during testing were fixed first (VSSDK1031 on deploy, missing package CodeBase); see implementation notes.

## US-0102 Logging to the Output window

**Status:** Done (accepted 2026-10-26)

As a user, I want errors and executed metadata queries logged in a separate Output pane, so that I can see what went wrong.

**Acceptance criteria**

- [x] Output pane "Object Explorer for MySQL" exists. *(manual test)*
- [x] Log levels Error, Warning, Info, Debug; Debug only when enabled in options. *(level filter unit tested; option is a manual test)*
- [x] Passwords never appear in the log (unit tested on the connection string formatter).

**Tasks**

- [x] T-0102-01 Logger abstraction in Core: `LogLevel`, `ILogSink`, `IExtensionLogger`, `ExtensionLogger` (level filter, fixed-width format, never throws)
- [x] T-0102-02 Output pane implementation in Vsix: `OutputWindowLogSink`, shared `ExtensionLog`, option *Debug logging* (Unified Settings), errors when opening the tool window are logged and shown in a message box
- [x] T-0102-03 Connection string masking + tests: `SensitiveDataMasker` masks `Password`, `Pwd`, `Passwd` and every key ending in `Password` (also quoted values with `;`); the logger masks every message and exception text

**Implementation notes**

- Entry format: `[14:05:09.123] INFO   message`. Exceptions follow on the next lines with their full stack trace.
- The pane is created on the UI thread on first use. Entries logged before that are buffered and written in order.
- Log text is English only, like Visual Studio's own diagnostic output (see ADR-005). The pane name and the option texts are localizable.
- The *Debug logging* option uses the VisualStudio.Extensibility settings API, which is marked preview in version 17.14 (`VSEXTPREVIEW_SETTINGS`). `DebugLoggingMonitor` reads the value and follows changes while Visual Studio runs. It is started from the View menu command (VisualStudio.Extensibility side), because the VSSDK package cannot get the `VisualStudioExtensibility` service (first test round: `ServiceUnavailableException`, option was never read).
- Second test round: starting the monitor from the command's `InitializeAsync` made the read wait forever without an error. It now starts (not awaited) when the menu item is clicked, read and subscribe each have a 10 second timeout, and the value read is always logged (`INFO   Option 'Debug logging' is on.`).
- The Output pane stays available after the explorer window is closed. That is intended: panes belong to the Output window, not to a tool window (like the Build or Git panes), and later background work such as refreshing a server keeps logging there.
- The WPF binding error about `PART_SearchButton` in the debug output comes from Visual Studio's own Options search box, not from this extension.
- 36 new unit tests (49 in total), all green.

**Manual test**

1. Rebuild the solution and press F5.
2. Open *View > Object Explorer for MySQL*, then *View > Output*. In "Show output from" choose "Object Explorer for MySQL". Expected: a line `[time] INFO   Object Explorer for MySQL loaded (assembly version ...)`.
3. Open *Tools > Options* and search for "Object Explorer for MySQL". Expected: a page with the checkbox "Debug logging", off by default, with a description.
4. Turn "Debug logging" on. Expected: the pane shows `INFO   Debug logging enabled.`
5. Close the explorer window and open it again via *View*. Expected: `DEBUG  Explorer tool window shown.`
6. Turn "Debug logging" off. Expected: `INFO   Debug logging disabled.` Reopening the explorer adds no DEBUG line.
7. Turn "Debug logging" on, close the Experimental Instance and start it again with F5. Open the explorer. Expected: DEBUG lines appear again (the option is saved).

**Test result**

2026-10-26, Herbert: accepted. Option value is read at start, switching on and off shows the expected lines immediately, the saved value is read again after a restart. Two issues found during testing were fixed first (settings service not available to the package; read hanging when started from command initialization).

## US-0103 Localization-ready resources

**Status:** Done (accepted 2026-10-26)

As a developer, I want all user-visible text in resource files that follow the Visual Studio language, so that a language can be added later without code changes.

*Scope changed on 2026-10-26 (ADR-010): Visual Studio has no Dutch user interface, so a Dutch translation would never be shown. Version 1 ships English only; this story makes sure adding a Visual Studio language later only needs resource files.*

**Acceptance criteria**

- [x] User-visible text of the tool window, messages and Output pane name is in `Resources/Strings.resx` (neutral = English), read through `Strings.cs`.
- [x] Command and option texts are in `.vsextension/string-resources.json`.
- [x] Unit tests fail when a key used in code is missing, a resource key is unused, a value is empty, or a language file (`Strings.<culture>.resx`, `.vsextension/<culture>/string-resources.json`) has missing or unknown keys.
- [x] `docs/Localization.md` describes where text lives and how to add a language.
- [x] The extension still shows English texts and works as before. *(manual test)*

**Tasks**

- [x] T-0103-01 Resource files and typed accessor (done in US-0101 and US-0102)
- [x] T-0103-02 `ResourceConsistencyTests` (5 tests; checked by temporarily adding an incomplete German resx and JSON file: both tests failed with the expected messages)
- [x] T-0103-03 ADR-010, `docs/Localization.md`, backlog decision D-1 updated

**Manual test**

1. Rebuild the solution and press F5.
2. Open *View > Object Explorer for MySQL*. Expected: menu item, window title and hint text in English, as before.
3. Open *Tools > Options*, search "Object Explorer for MySQL". Expected: option "Debug logging" with its description in English.

**Test result**

2026-10-26, Herbert: accepted.
## US-0104 Build pipeline

**Status:** Ready for test

As a developer, I want GitHub Actions to build the solution and run unit tests on every push, so that broken builds are noticed.

**Acceptance criteria**

- [x] Workflow on a Windows runner with Visual Studio 2026: restore, build Release, run Core.Tests.
- [x] VSIX file published as build artifact.
- [x] Build badge in README.
- [x] The build fails on any compiler or analyzer warning (`-warnaserror`), so the "no warnings" rule of the Definition of Done is checked automatically.

**Tasks**

- [x] T-0104-01 `.github/workflows/build.yml`
- [x] T-0104-02 Badge in README

**Implementation notes**

- Runner `windows-2025`: GitHub moved this image to Visual Studio 2026 in June 2026. `microsoft/setup-msbuild` requires version `[18.0,)`, so the build fails clearly if the image ever lacks Visual Studio 2026.
- Triggers: push to `main` and to story branches `us-*`, pull requests to `main`, and manual start (*Run workflow*).
- The .NET SDK comes from `global.json`, so CI and local builds use the same SDK and the same test runner (Microsoft.Testing.Platform).
- Artifact `ObjectExplorerForMySql-vsix`, kept 30 days.
- The repository is private, so the badge is only visible to people with access to the repository.
- First run on branch `us-0104-build-pipeline`: green in 2m27s, 54 of 54 tests passed, VSIX artifact 1.4 MB.
- Workflow change: this story is developed on branch `us-0104-build-pipeline`, because a pipeline can only be tested on GitHub. After acceptance the branch is merged into `main` (fast-forward) and deleted.

**Manual test**

1. Open the repository on GitHub, tab *Actions*, workflow *Build*. Expected: a green run for branch `us-0104-build-pipeline`.
2. Open the run, section *Artifacts*: download `ObjectExplorerForMySql-vsix`, unzip it, and double-click `ObjectExplorerForMySql.vsix`. Expected: the VSIX installer offers "Object Explorer for MySQL" for Visual Studio 2026. You can cancel the installation; installing in your normal Visual Studio is also fine and can be undone in *Manage Extensions*.
3. Optional: *Run workflow* on the *Build* page starts a run manually. Expected: green.
4. After the merge into `main`: the badge at the top of the README shows "passing".

**Test result**

_To be filled in by Herbert._