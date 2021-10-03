#!/bin/bash
python3 -m venv local_lib/
source local_lib/bin/activate

pip --version

pip3 install --log pip_install.log --upgrade pip --force-reinstall git+https://github.com/jaraco/path.py.git

python3 my_program.py