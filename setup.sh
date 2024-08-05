#!/bin/bash

# Creates venv and installs packages in requiremements.txt
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi


source venv/bin/activate

if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
fi

# Execute main.py
python3 main.py