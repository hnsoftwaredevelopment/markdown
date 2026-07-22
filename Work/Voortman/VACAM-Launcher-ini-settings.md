# VACAM Launcher — `VACAM Launcher.exe.ini` settings reference

This document describes every setting the **VACAM Launcher** reads from (or writes to)
its `VACAM Launcher.exe.ini` file, based on an analysis of the source code in this
repository.

> Generated from source analysis. When in doubt, the source of truth is
> `VacamLauncher/Settings/Ini.cs` plus the classes that call `GetValue` / `SetValue`.

## How the INI file works

* Settings are read/written through the `Ini` class
  (`VacamLauncher/Settings/Ini.cs`), which wraps the Win32
  `GetPrivateProfileString` / `WritePrivateProfileString` API.
* Every read goes through `GetValue(section, entry, defaultValue)`. **If a key is
  missing, the coded default is used** — so the INI only needs to contain the values
  you want to override.
* Values are plain text. Booleans are stored as `True` / `False`. Integers are stored
  as text. Removing a key (or setting it to null in code) deletes the entry.

### Where the file lives

* Normally the launcher uses the file named `VACAM Launcher.exe.ini` next to the
  executable.
* If the path is **not** rooted/found, it resolves to the per-user location:
  `%LocalAppData%\<CompanyName>\VACAM Launcher\VACAM Launcher.exe.ini`
  (`Ini.GetApplicationDataFolder`).

### How settings are edited

* Only **two** settings are exposed in the **Options** dialog: the *Setup path*
  (`[Paths] Setups`) and the *Temp path* (`[Paths] Applications`).
* Everything else is edited by hand. The launcher has an **Edit ini file** menu item
  that simply opens this INI in the default text editor
  (`VacamLauncherSettingsEditor`).
* Some settings are also toggled indirectly via menu items / checkboxes (noted per
  setting below).

## Legend

* **Type** — how the value is interpreted in code (`string`, `bool`, `int`, `enum`).
* **Default** — value used when the key is absent.
* **Read in** — the class/property that consumes the setting.

---

## `[Paths]`

Filesystem locations the launcher works with.

| Key | Type | Default | Purpose |
|-----|------|---------|---------|
| `Setups` | string | `\\vaSoftware\Setups\VACAM` | Root folder where VACAM setups (installers) are found. Editable via **Options → Setup path**. Validated on load: if it is a network path it is normalized back to the standard EU path (`\\vaSoftware\Setups\VACAM`) or, for the US, `\\vc-fs-svr01\officefiles$\Service\Vacam Installations`. |
| `Applications` | string | *(empty → falls back to `C:\Temp\`)* | Temp/working folder used for extracted files, drag-drop, SQLite packaging, etc. Editable via **Options → Temp path**. Read through `Functions.TempPath`. |
| `SolutionsBaseFolder` | string | `C:\git` | Base folder scanned for VACAM source solutions (source-based start). Read through `Functions.SolutionsBaseFolder`. |
| `VasimSolutionFolder` | string | `C:\git\VASIM\VASIM` | Folder containing `VASIM.sln`, used when starting VASIM from source. Read through `Vasim.GetSolution()`. |

## `[Database]`

SQL Server connection the launcher uses, and which it propagates into the
`VACAM.exe.ini` and `VASIM.exe.ini` files when starting those apps.

| Key | Type | Default | Purpose |
|-----|------|---------|---------|
| `Server` | string | `127.0.0.1\CAM2022` | SQL Server instance (`host\instance`). Used to locate the DB server, build connection strings, and is written into VACAM/VASIM ini. *(Note: one legacy code path in `GetConnectionString` defaults to `127.0.0.1\CAM2014` if the key is missing.)* |
| `User` | string | `VACAM-User` | SQL login the launcher configures/uses for VACAM & VASIM. |
| `Password` | string | `vacon02` | Password for `User`. |

> **Not read by the launcher (see “Unused / legacy keys” below):**
> `IntegratedSecurity` and `SaPwd` in `[Database]` are present in the sample INI but
> are not read from the launcher's own INI. `IntegratedSecurity` is always written as
> `false` into the VACAM/VASIM ini, and the `sa` password used for packaging is
> hard-coded, not taken from `SaPwd`.

## `[ConfigDatabase]` and `[LogDatabase]`

These sections appear in the sample INI but are **not read from the launcher's own
INI**. The launcher *generates* these sections inside the target `VACAM.exe.ini`
(and VASIM's ini) at start time, using the `[Database]` credentials above together
with database names it computes from the selected backup. You normally do not need to
set them here.

## `[PLC]`

TwinCAT / ADS settings for the local (simulation) runtime.

| Key | Type | Default | Purpose |
|-----|------|---------|---------|
| `Tc3AmsNetId` | string | *(empty)* | Local TwinCAT 3 AMS Net Id used by the launcher. Read through `VacamLauncherSettings.LocalAmsNetId`. |
| `Tc3AdsPort` | int | `851` | Local TwinCAT 3 ADS port. Read through `VacamLauncherSettings.LocalAdsPort`. |
| `RuntimeMode` | enum | `Auto` | TwinCAT runtime to use: `Auto`, `Kernel`, or `Usermode`. Selectable from the **TwinCAT runtime** menu, but only when both a user-mode and a kernel runtime are detected. Read through `VacamLauncherSettings.RuntimeMode`. |
| `MainTaskCycleTime` | int | `10` | Main-task cycle time (ms) applied to the TwinCAT project when it is modified for simulation. Read through `VacamLauncherSettings.MainTaskCycleTime`. |

> **Not read by the launcher:** the plain `AmsNetId` and `AdsPort` keys in `[PLC]`
> (as seen in the sample INI) are legacy. The launcher reads `Tc3AmsNetId` /
> `Tc3AdsPort` for its own runtime and only *writes* `AmsNetId` / `AdsPort` into the
> VACAM/VASIM ini files.

## `[Settings]`

General launcher behaviour flags. All are booleans (`True` / `False`).

| Key | Type | Default | Purpose |
|-----|------|---------|---------|
| `EnableLogging` | bool | `True` | Enables logging and makes the **Log** menu item visible. This is the only setting here that defaults to **True**. |
| `ForceX86` | bool | `False` | Forces the launcher to run VACAM in 32-bit (x86) mode. Read through `VacamLauncherSettings.ForceX86`. (Distinct from `[SQLite] ForceX86`.) |
| `ShowDepricateFeatures` | bool | `False` | Shows deprecated/legacy features in the UI (extra options, git tags, etc.). *(Key name is misspelled in code as “Depricate”.)* |
| `RestoreVacamDatabase` | bool | `False` | When set, restores the VACAM database from the backup as part of preparing/starting. |
| `GetLatest` | bool | `False` | Gets the latest sources/version before starting (source-based flow). |
| `StartInVisualStudio` | bool | `False` | Opens the selected .NET solution in Visual Studio for debugging instead of just running it. Also toggled by the “debug .NET” checkbox in the UI. |
| `ForceRelease` | bool | `False` | Forces a Release build of the .NET solution (instead of Debug). Also toggled in the UI. |
| `DropBackups` | bool | `False` | Enables the “drop backups” behaviour/menu item. Read-only in code (no setter). |
| `ChooseLanguage` | bool | `False` | If `True`, VACAM prompts for language at startup. If `False`, the launcher configures VACAM for silent login with language `EN`. |
| `IgnoreVpnActive` | bool | `False` | Skips the “VPN is active” safety check. Set to `True` to suppress the VPN warning. |
| `VasimInDebugger` | bool | `False` | Starts VASIM under the debugger (source flow). Read through `Vasim.SettingVasimInDebugger`. |
| `StartVasimRc` | bool | `False` | If `True`, the “live” VASIM version is the **RC** build; otherwise the **Master** build. Read through `Vasim.GetLiveVersion()`. |

> **Not read by the launcher:** `PreferTfsOverUnc` appears in the sample INI but is not
> referenced anywhere in the current code (legacy from the TFS-vs-UNC era).

## `[SQLite]`

| Key | Type | Default | Purpose |
|-----|------|---------|---------|
| `ForceX86` | bool | `False` | Forces 32-bit (x86) when creating the SQLite package/databases. Toggled by the **Force SQLite x86** menu item. Read through `Functions.SettingForceSqliteX86`. |

## `[Git]`

| Key | Type | Default | Purpose |
|-----|------|---------|---------|
| `ShowGitTags` | bool | `False` | Shows git tags in the .NET/source solution selector. Read through `Functions.ShowGitTagsDotNet`. |

## `[misc]`

| Key | Type | Default | Purpose |
|-----|------|---------|---------|
| `Configurator` | bool | `False` | Enables “configurator” mode (checks the **Configurator** menu item). Read through `Functions.IsConfigurator`. |

## `[TwinCat]`

Which TwinCAT loader is used, and the remembered source per loader.

| Key | Type | Default | Purpose |
|-----|------|---------|---------|
| `SelectedLoader` | string | `SkipTwinCat` | Which TwinCAT loader to use. One of `TwinCatFromSetup`, `TwinCatFromSource`, or `SkipTwinCat`. Any unknown value falls back to `SkipTwinCat`. |
| `TwinCatFromSetup` | string | *(none)* | Remembered “selected source” for the *from setup* loader. Written via `SetSelectedSource`. |
| `TwinCatFromSource` | string | *(none)* | Remembered “selected source” for the *from source* loader. Written via `SetSelectedSource`. |

## `[Selection]`

Remembered “last used” selections, written automatically by the launcher so your
choices persist between sessions. You normally do not edit these by hand.

| Key | Type | Purpose |
|-----|------|---------|
| `LastSelectedEquipmentNumber` | string | Last equipment number chosen. |
| `LastSelectedProjectNumber` | string | Last project number chosen. |
| `LastSelectedMachineName` | string | Last machine name chosen. |
| `LastSelectedCustomerName` | string | Last customer name chosen. |
| `LastSelectedYear` | string | Last year chosen. |
| `LastSelectedSetupInfo` | string | Path to the last selected setup. |
| `LastSelectedSolution` | string | Path to the last selected source solution. |

## `[Customers]`

A **dynamic** section: there is no fixed list of keys. Each entry name is a customer
location (lower-cased) and the value is a boolean enabling/disabling that location.
Managed via `Functions.GetCustomerLocationEnabled` / `SetCustomerLocationEnabled`.

```ini
[Customers]
somelocation=True
anotherlocation=False
```

## `[VacamLaucherForm]`

Window position/size, saved automatically on exit and restored on start. You normally
do not edit these by hand. *(The section name is spelled `VacamLaucherForm` in code —
note the missing “n”.)*

| Key | Type | Purpose |
|-----|------|---------|
| `Left` | int | Window X position. |
| `Top` | int | Window Y position. |
| `Width` | int | Window width. |
| `Height` | int | Window height. |

---

## Unused / legacy keys (safe to ignore)

These keys appear in the shipped sample INI but are **not read anywhere** in the
current launcher code. They are kept here so you know they can be removed or ignored:

| Section | Key | Note |
|---------|-----|------|
| `[Settings]` | `PreferTfsOverUnc` | Not referenced in code. |
| `[Database]` | `SaPwd` | Not referenced in code; the `sa` password is hard-coded where needed. |
| `[Database]` / `[ConfigDatabase]` / `[LogDatabase]` | `IntegratedSecurity` | Not read from the launcher INI; always written as `false` into VACAM/VASIM ini. |
| `[PLC]` | `AmsNetId`, `AdsPort` | Legacy; launcher uses `Tc3AmsNetId` / `Tc3AdsPort` instead. |
| `[ConfigDatabase]`, `[LogDatabase]` | *(all keys)* | Generated into VACAM/VASIM ini at start; not read from the launcher INI. |

## Related note: MSI version cache (separate file)

`MsiVersionCache` also uses the INI format, but with a **separate** cache file (not
`VACAM Launcher.exe.ini`). It stores one section per setup file (section name = the
setup's full path) with `Version` and `LastWriteTime` entries, so it can skip
re-reading the version from unchanged MSI files. This is an implementation cache and
is not meant to be edited by hand.

## Related note: what gets written to VACAM.exe.ini / VASIM.exe.ini

When starting VACAM or VASIM, the launcher writes a matching configuration into the
*target* app's own INI (`VACAM.exe.ini` / `VASIM.exe.ini`), including `[Database]`,
`[ConfigDatabase]`, `[LogDatabase]`, `[PLC]`, and `[Application]` sections derived from
the settings above plus the selected backup. Those files are regenerated on each start,
so editing them directly is not persistent — change the launcher settings instead.

---

## Minimal example

A minimal `VACAM Launcher.exe.ini` typically only needs the paths and database server:

```ini
[Paths]
Setups=\\vaSoftware\Setups\VACAM
Applications=C:\Temp\
SolutionsBaseFolder=C:\git\

[Database]
Server=127.0.0.1\CAM2022
User=VACAM-User
Password=vacon02

[PLC]
Tc3AdsPort=851
```
