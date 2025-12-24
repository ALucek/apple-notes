#!/usr/bin/env python3
"""
Delete a single note from the agent-notes folder.

Arguments:
    --title: Note title to delete (required)

Usage:
    python delete-note.py --title "My Note"
"""
import argparse
import subprocess

FOLDER = "agent-notes"

parser = argparse.ArgumentParser(description="Delete a note from agent-notes folder")
parser.add_argument("--title", required=True, help="Note title to delete")
args = parser.parse_args()

title = args.title.replace('"', '\\"')

script = f'''
tell application "Notes"
    if not (exists folder "{FOLDER}") then
        return "Folder not found"
    end if
    try
        delete (first note of folder "{FOLDER}" whose name is "{title}")
        return "Deleted: {title}"
    on error
        return "Note not found: {title}"
    end try
end tell
'''

result = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
print(result.stdout.strip())

