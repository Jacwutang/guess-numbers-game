#!/bin/bash

# Create venv if not already exists
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

source venv/bin/activate

# Install packages
if [ -f "requiremements.txt" ]; then
    pip install -r requirements.txt
fi


# Run tests
pytest -vv