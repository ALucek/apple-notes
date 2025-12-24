# Apple Notes Plugin

A Claude Code plugin for interacting with Apple Notes. Enables persistent storage and retrieval of information using the native Notes app on macOS.

## Installation

Add this marketplace to Claude Code:

```
/plugin marketplace add ALucek/apple-notes
```

Then install the plugin:

```
/plugin install apple-notes@apple-notes-marketplace
```

## What It Does

Provides CRUD operations for Apple Notes, scoped to an `agent-notes` folder:

- **List** all notes in the folder
- **Create** new notes with HTML formatting
- **Read** note content as HTML
- **Delete** notes by title

Notes persist across sessions and sync via iCloud.

## Requirements

- macOS with Apple Notes
- Python 3
- Claude Code

## Documentation

See the [SKILL.md](plugins/apple-notes/skills/apple-notes/SKILL.md) for full usage documentation including HTML formatting reference.

## License

MIT
