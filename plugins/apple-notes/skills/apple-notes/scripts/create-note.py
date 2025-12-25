#!/usr/bin/env python3
"""
Create a new note in the agent-notes folder.

Supports HTML formatting in the body. Creates the folder if it doesn't exist.
Title is automatically formatted as an <h1> header.

Arguments:
    --title: Note title (required)
    Body content is read from stdin (HTML format)

Usage:
    echo "<div>Content</div>" | python create-note.py --title "My Note"
"""
import argparse
import subprocess
import sys

FOLDER = "agent-notes"

parser = argparse.ArgumentParser(description="Create a note in agent-notes folder")
parser.add_argument("--title", required=True, help="Note title")
args = parser.parse_args()

body = sys.stdin.read().strip()
title = args.title.replace('"', '\\"')
body = body.replace('"', '\\"')

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
