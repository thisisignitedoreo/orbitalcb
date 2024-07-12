#!/bin/sh

set -xe

~/.local/bin/pyside6-uic main.ui -o ui_main.py
~/.local/bin/pyside6-rcc main.qrc -o main_rc.py

python -m PyInstaller Orbital.spec
python -m nuitka --onefile cmd.py

rm -r cmd.build cmd.dist build
mv dist/Orbital ./
mv cmd.bin OrbitalCmd
rm -r dist
