@echo off

pyside6-uic main.ui -o ui_main.py
pyside6-rcc main.qrc -o main_rc.py

pyinstaller Orbital.spec
