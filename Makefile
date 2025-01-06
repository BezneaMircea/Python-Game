# Variables
PYTHON := python
VENV := .venv
VENV2 := ..\$(VENV)
ACTIVATE := $(VENV)\Scripts\activate.bat
MAIN := StartGame.py
SRC_DIR := src

# Default target
all: run

# Ensure pip is installed
get-pip:
	@echo "Checking for pip..."
	@if not exist "$(PYTHON)\Scripts\pip.exe" ($(PYTHON) -m ensurepip --upgrade || @echo "Error: Failed to install pip.") && @echo "pip installed."

# Create a virtual environment
$(VENV)\Scripts\activate.bat:
	$(PYTHON) -m venv $(VENV)

# Install dependencies (pygame and numpy)
install: $(ACTIVATE) get-pip
	$(ACTIVATE) && $(PYTHON) -m pip install --upgrade pip setuptools
	$(ACTIVATE) && $(PYTHON) -m pip install pygame numpy
	@echo "Dependencies installed: pygame, numpy"

# Run the game (ensure it's executed from the src directory)
run: $(ACTIVATE)
	@echo "Running the game from the src directory..."
	@cd $(SRC_DIR) && call $(VENV2)\Scripts\activate.bat && $(PYTHON) $(MAIN)

# Freeze dependencies into requirements.txt
freeze: $(ACTIVATE)
	$(ACTIVATE) && $(PYTHON) -m pip freeze > requirements.txt
	@echo "Dependencies saved to requirements.txt"

# Clean up the virtual environment
clean:
	@if exist $(VENV) rmdir /s /q $(VENV)
	@echo "Virtual environment removed."
	@echo "Removing __pycache__ directories..."
	@del /s /q $(SRC_DIR)\__pycache__ 2> nul
	@for /r $(SRC_DIR) %%d in (__pycache__) do rmdir /s /q "%%d" 2> nul
	@echo "All __pycache__ directories removed."

# Help command to list all tasks
help:
	@echo "Makefile for managing the Python project (Windows)"
	@echo "Available commands:"
	@echo "  make install     - Create the virtual environment and install dependencies"
	@echo "  make run         - Run the main application"
	@echo "  make freeze      - Freeze dependencies into requirements.txt"
	@echo "  make clean       - Remove the virtual environment"
	@echo "  make get-pip     - Ensure pip is installed"
