#!/bin/bash
cd "$(dirname "$0")"
source venv/bin/activate
export $(grep -v '^#' .env | xargs)
python src/server.py