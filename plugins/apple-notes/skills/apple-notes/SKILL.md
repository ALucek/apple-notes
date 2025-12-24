---
name: apple-notes
description: Interact with the Apple Notes app. CRUD operations for persistent storage of thoughts, data, and information across sessions.
license: MIT License
metadata:
  author: "lucek.ai"
  version: "1.0.0"
---

# Apple Notes Creation & Editing

## Overview

Tools to interact with Apple Notes. Notes are scoped to an automatically created `agent-notes` folder. Notes are formatted using HTML—supported elements are listed below.

## When to Use

- Storing information that should persist across sessions
- Saving notes, ideas, or data the User wants to keep
- Creating task lists, reminders, or reference material
- When the User explicitly asks to save/remember something in notes

## How to Use

1. **List** existing notes to see what's available
2. **Read** a note to get its HTML content
3. **Create** new notes with HTML-formatted body
4. **Delete** notes by title (to edit: read → delete → create)

## Usage

```bash
python scripts/list-notes.py
python scripts/create-note.py --title "Note" --body "<div>Content</div>"
python scripts/read-note.py --title "Note"
python scripts/delete-note.py --title "Note"
```

> **Note:** The `--title` is automatically formatted as an `<h1>` header at the top of the note. Only include body content in `--body`.

## HTML Reference

| Element | HTML | Example |
|---------|------|---------|
| Title | `<h1>` | `<h1>Title</h1>` |
| Heading | `<h2>` | `<h2>Heading</h2>` |
| Subheading | `<h3>` | `<h3>Subheading</h3>` |
| Paragraph | `<div>` | `<div>Text here</div>` |
| Bold | `<b>` | `<b>bold</b>` |
| Italic | `<i>` | `<i>italic</i>` |
| Underline | `<u>` | `<u>underline</u>` |
| Strikethrough | `<strike>` | `<strike>deleted</strike>` |
| Monospace | `<tt>` | `<tt>code</tt>` |
| Line break | `<br>` | `<br>` |
| Bullet list | `<ul><li>` | `<ul><li>Item 1</li><li>Item 2</li></ul>` |
| Numbered list | `<ol><li>` | `<ol><li>First</li><li>Second</li></ol>` |
| Table | `<object><table>` | See below |

### Table Example
```html
<object><table><tbody><tr><td>A</td><td>B</td></tr><tr><td>1</td><td>2</td></tr></tbody></table></object>
```

## Limitations

The following capabilities of Apple Notes are not available:

- **Checklists** - Stored internally, checkbox state not accessible (renders as regular bullet list)
- **Links** - Stripped on save
- **Highlights** - Stored internally by Apple Notes
- **Images** - Technically possible (base64) but impractical for LLM use
- **Attachments** - Cannot be added programmatically

