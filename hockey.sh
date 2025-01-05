#!/bin/bash
echo "Configuring environment..."
pip install --upgrade --quiet pip
pip install --quiet -r requirements.txt

echo "Launching the game..."
cd src/menus
python3 StartMenu.py
cd ../..
find ./src/menus -type d -name "__pycache__" -exec rm -r {} +

