#!/bin/sh
python3 -m venv django_venv
source django_venv/bin/activate

pip install -r requirement.txt
deactivate