#!/bin/bash

SCRIPT_PATH=$(dirname `which $0`)
cd $SCRIPT_PATH/..
rm dist/* || true
python3 setup.py bdist_wheel
pip3 uninstall -y filip_python_economy
pip3 install dist/filip_python_economy-0.0.1-*
cd scripts
