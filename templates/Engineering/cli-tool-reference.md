# My Document

**Version:** 1.0.0
**Last Updated:** YYYY-MM-DD

---

## Installation

```bash
brew install tool-name
# or
npm install -g tool-name
```

## Global Options

| Flag | Short | Description |
|------|-------|-------------|
| `--help` | `-h` | Show help message |
| `--version` | `-v` | Show version |
| `--verbose` |  | Enable verbose output |
| `--config` | `-c` | Path to config file |

## Commands

### `init`

Initialize a new project.

```bash
tool-name init [options]
```

| Option | Default | Description |
|--------|---------|-------------|
| `--template` | default | Project template |
| `--name` | | Project name |

### `build`

Build the project.

```bash
tool-name build [options]
```

| Option | Default | Description |
|--------|---------|-------------|
| `--output` | ./dist | Output directory |
| `--watch` | false | Watch for changes |

### `deploy`

Deploy to a target environment.

```bash
tool-name deploy --env <environment>
```

## Examples

```bash
# Create a new project
tool-name init --name my-project

# Build and watch
tool-name build --watch

# Deploy to staging
tool-name deploy --env staging
```
