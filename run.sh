#!/usr/bin/env bash

set -xe

~/.local/bin/pyside6-uic main.ui -o ui_main.py
~/.local/bin/pyside6-rcc main.qrc -o main_rc.py

python main.py

