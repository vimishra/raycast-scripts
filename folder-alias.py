#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Folder Alias
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 🤖
# @raycast.argument1 { "type": "text", "placeholder": "home", "percentEncoded": false }

# Documentation:
# @raycast.description Open a Folder based on a previously created alias
# @raycast.author Vikas Mishra
# @raycast.authorURL https://github.com/vimishra

import json
import sys
import os

# First open the config file and convert it into a dict
with open('/Users/vikasmis/.config/folder-alias.json') as f:
    data = f.read()

folders = json.loads(data)

# Check to see if the argument matches a key in the dict.
if sys.argv[1] in folders:
    # print(f"Folder Expanded: {folders[sys.argv[1]]}")
    os.system(f"open \"{folders[sys.argv[1]]}\"")
else:
    print("Folder Not Found")

# If it does, open it.
# If it doesn't, echo a message indicating "Folder not found."
