#!/bin/bash
echo "Configuring environment..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Launching the game..."
cd src/menus
python3 StartMenu.py
cd ../..