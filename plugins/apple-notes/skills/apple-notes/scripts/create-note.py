#!/usr/bin/env python3
"""
Create a new note in the agent-notes folder.

Supports HTML formatting in the body (bold, italic, lists, tables, etc).
Creates the folder if it doesn't exist.

Arguments:
    --title: Note title (required)
    --body: Note body with HTML formatting (required)

Usage:
    python create-note.py --title "My Note" --body "<div>Content here</div>"
"""
import argparse
import subprocess

FOLDER = "agent-notes"

parser = argparse.ArgumentParser(description="Create a note in agent-notes folder")
parser.add_argument("--title", required=True, help="Note title")
parser.add_argument("--body", required=True, help="Note body (HTML Format)")
args = parser.parse_args()

title = args.title.replace('"', '\\"')
body = args.body.replace('"', '\\"')

script = f'''
tell application "Notes"
    if not (exists folder "{FOLDER}") then
        make new folder with properties {{name:"{FOLDER}"}}
    end if
    make new note at folder "{FOLDER}" with properties {{body:"<h1>{title}</h1><br>{body}"}}
    return "Created: {title}"
end tell
'''

result = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
print(result.stdout.strip() if result.returncode == 0 else f"Error: {result.stderr}")

