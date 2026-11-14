# Object Explorer for MySQL

[![Build](https://github.com/hnsoftwaredevelopment/ObjectExplorerForMySQL/actions/workflows/build.yml/badge.svg?branch=main)](https://github.com/hnsoftwaredevelopment/ObjectExplorerForMySQL/actions/workflows/build.yml)

A Visual Studio 2026+ extension that adds a MySQL object explorer, modeled on the built-in SQL Server Object Explorer.

Connect to one or more MySQL servers, browse databases, tables, columns, keys, constraints, indexes, triggers, views, stored procedures, functions and events, inspect their properties in the Visual Studio Properties window, and drag object names into your code without typos.

> Not affiliated with or endorsed by Oracle Corporation. MySQL is a trademark of Oracle and/or its affiliates.

## Status

In development (release 0.1). See the [backlog](docs/backlog/Backlog.md).

## Requirements

- Visual Studio 2026 (version 18.0) or later
- MySQL 8.0 or later, including 8.4 LTS (MariaDB 10.6+ best effort)

## Building

You need Visual Studio 2026 with the *Visual Studio extension development* workload and the .NET 10 SDK.

- Open `ObjectExplorerForMySql.slnx`, set `ObjectExplorerForMySql.Vsix` as startup project and press F5 to start the Experimental Instance.
- Command line: build with Visual Studio's `MSBuild.exe ObjectExplorerForMySql.slnx -restore`; run tests with `dotnet test --project tests\ObjectExplorerForMySql.Core.Tests`.

## Documentation

| Document | Content |
|---|---|
| [docs/Architecture.md](docs/Architecture.md) | Technical decisions (ADRs) |
| [docs/Workflow.md](docs/Workflow.md) | Definition of Done, commit and push rules, test split |
| [docs/Localization.md](docs/Localization.md) | Where text lives and how to add a language |
| [docs/backlog/Backlog.md](docs/backlog/Backlog.md) | Epics, user stories and status |

## Repository layout (planned)

```
src/
  ObjectExplorerForMySql.Core/        Metadata access, models, script generation (no VS dependency)
  ObjectExplorerForMySql.Vsix/        Visual Studio extension (tool window, commands, editor integration)
tests/
  ObjectExplorerForMySql.Core.Tests/  Unit tests
  ObjectExplorerForMySql.IntegrationTests/  Tests against a real MySQL server (optional, Docker, planned)
docs/
```

## License

[MIT](LICENSE)
