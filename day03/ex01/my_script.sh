#!/bin/sh
python3 -m venv library/
source library/bin/activate

pip3 --version
# pip install --upgrade pip
# pip install git+https://github.com/jaraco/path.git

pip3 install --log pip_install.log --upgrade pip --force-reinstall git+https://github.com/jaraco/path.py.git
# mv -f "./library/lib/python3.8/site-packages/path" ./
# # mv -rf /lib/lib ./
# rm -rf library

python3 my_program.py