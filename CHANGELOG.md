# Changelog

## [1.2.1] - 2025-12-29

### Changed
- Exclamation escaping handling with create note 

## [1.2.0] - 2025-12-25

### Changed
- Standardized on heredoc (`<< 'EOF'`) for reliable input handling
- Updated docs and examples to use heredoc pattern

## [1.1.0] - 2025-12-25

### Changed
- `create-note.py` now reads body content from stdin to avoid shell escaping issues

### Fixed
- Improved AppleScript escaping for special characters (backslashes, quotes)

## [1.0.0] - 2025-12-24

### Added
- `list-notes.py` - List all notes in the agent-notes folder
- `create-note.py` - Create notes with HTML formatting
- `read-note.py` - Read note content as HTML
- `delete-note.py` - Delete notes by title
- Auto-creation of `agent-notes` folder
- HTML formatting support (headings, lists, tables, text styling)
- SKILL.md with usage docs and HTML reference
