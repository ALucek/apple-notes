#!/usr/bin/env python3
"""
Read a note from the agent-notes folder. Returns the note body as HTML.

Arguments:
    --title: Note title to read (required)

Usage:
    python read-note.py --title "My Note"
"""
import argparse
import subprocess

FOLDER = "agent-notes"

parser = argparse.ArgumentParser(description="Read a note from agent-notes folder")
parser.add_argument("--title", required=True, help="Note title to read")
args = parser.parse_args()

title = args.title.replace('"', '\\"')

script = f'''
tell application "Notes"
    if not (exists folder "{FOLDER}") then
        return "Folder not found"
    end if
    try
        set n to first note of folder "{FOLDER}" whose name is "{title}"
        return body of n
    on error
        return "Note not found: {title}"
    end try
end tell
'''

result = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
print(result.stdout.strip())