#!/bin/bash

echo "=== Project Analysis ==="

# Get file count
copilot -p "Count all .py files recursively and report" --allow-tool 'shell'

echo ""
echo "=== Code Quality Check ==="

# Check for issues
copilot -p "Look for any TODO comments in Python files" --allow-tool 'shell'
