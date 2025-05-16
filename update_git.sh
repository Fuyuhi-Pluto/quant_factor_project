#!/bin/bash

# Default commit message if none is provided

MESSAGE=${1:-"Update project"}

echo "Adding all files..."
git add .

echo "Committing with message: $MESSAGE"
git commit -m "$MESSAGE"

echo "Pushing to GitHub..."
git push origin main

echo "All done!"

