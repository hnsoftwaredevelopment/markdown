# E01 Foundation

Set up the solution, build, logging and localization so all later stories build on the same base.

## US-0101 Solution and empty extension

**Status:** Ready for test

As a developer, I want a solution that builds a VSIX which installs in Visual Studio 2026, so that every following story has a working base.

**Acceptance criteria**

- [x] Solution `ObjectExplorerForMySql.slnx` with projects Core (`netstandard2.0`), Vsix (`net48`), Core.Tests (`net10.0`).
- [x] VSIX manifest: name "Object Explorer for MySQL", installation target `[18.0,)` (amd64 and arm64), publisher hnsoftwaredevelopment, MIT license included.
- [ ] F5 starts the Experimental Instance with the extension loaded. *(manual test)*
- [ ] Menu item *View > Object Explorer for MySQL* opens an empty, dockable tool window. *(manual test)*
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

_To be filled in by Herbert._

## US-0102 Logging to the Output window

**Status:** Todo

As a user, I want errors and executed metadata queries logged in a separate Output pane, so that I can see what went wrong.

**Acceptance criteria**

- [ ] Output pane "Object Explorer for MySQL" exists.
- [ ] Log levels Error, Warning, Info, Debug; Debug only when enabled in options.
- [ ] Passwords never appear in the log (unit tested on the connection string formatter).

**Tasks**

- T-0102-01 `ILogger` abstraction in Core
- T-0102-02 Output pane implementation in Vsix
- T-0102-03 Connection string masking + tests

## US-0103 Localization infrastructure

**Status:** Todo

As a user, I want the extension in my Visual Studio language (English or Dutch), so that it matches the rest of my IDE.

**Acceptance criteria**

- [ ] `Resources.resx` (neutral = English) and `Resources.nl.resx` in Vsix.
- [ ] Command texts localized via `string-resources.json` per language.
- [ ] VSIX manifest display name and description localized.
- [ ] With Visual Studio set to Dutch, menu and tool window texts are Dutch; with any other language they are English.
- [ ] Unit test that every key in the neutral resx exists in each language resx.

**Tasks**

- T-0103-01 Resource files and strongly typed accessor
- T-0103-02 Localized command and manifest strings
- T-0103-03 Resource completeness test

**Manual test**

1. *Tools > Options > Environment > International Settings*: set Nederlands (language pack required), restart.
2. Expected: tool window title and menu item are Dutch.

## US-0104 Build pipeline

**Status:** Todo

As a developer, I want GitHub Actions to build the solution and run unit tests on every push, so that broken builds are noticed.

**Acceptance criteria**

- [ ] Workflow on `windows-latest`: restore, build Release, run Core.Tests.
- [ ] VSIX file published as build artifact.
- [ ] Build badge in README.

**Tasks**

- T-0104-01 `.github/workflows/build.yml`
- T-0104-02 Badge in README
