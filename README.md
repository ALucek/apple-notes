# Apple Notes Skill

An agent skill for interacting with Apple Notes. Enables LLMs to persistently store and retrieve information using the native Notes app on macOS.

## What It Does

Provides CRUD operations for Apple Notes, scoped to an `agent-notes` folder. Notes persist across sessions and sync via iCloud.

## Usage

See [SKILL.md](SKILL.md) for full documentation including HTML formatting reference.

```bash
python scripts/list-notes.py                              # List all notes
python scripts/create-note.py --title "X" --body "<html>" # Create note
python scripts/read-note.py --title "X"                   # Read note (HTML)
python scripts/delete-note.py --title "X"                 # Delete note
```

## Requirements

- macOS with Apple Notes
- Python 3

## License

MIT