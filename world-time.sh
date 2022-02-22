#!/usr/bin/env bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title World Time
# @raycast.mode inline
# @raycast.refreshTime 5s
# @raycast.packageName Dashboard

# Optional parameters:
# @raycast.icon 🕐
#
# Documentation:
# @raycast.description Show the time from elsewhere in the world
# @raycast.author Jesse Claven
# @raycast.authorURL https://github.com/jesse-c

# Timezones can be found in /usr/share/zoneinfo

bay=$(TZ=America/Los_Angeles date +"%l:%M %p")
israel=$(TZ=Asia/Jerusalem date +"%l:%M %p")
penang=$(TZ=Asia/Kuala_Lumpur date +"%l:%M %p")

echo "Mountain View: $bay | Jerusalem: $israel | Penang: $penang"
