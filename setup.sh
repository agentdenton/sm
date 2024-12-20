#!/usr/bin/bash -eu

direnv allow .

if [ ! -d "venv" ]; then
    python -m venv venv
fi
