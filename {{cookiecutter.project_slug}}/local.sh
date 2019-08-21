#!/usr/bin/env bash
python3 -m venv venv
source "venv/bin/activate"
pip install -r requirements-dev.txt
ve() { source $1/bin/activate; }