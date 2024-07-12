@echo off

pyside6-uic main.ui -o ui_main.py
pyside6-rcc main.qrc -o main_rc.py

pyinstaller Orbital.spec
nuitka --windows-icon-from-ico=assets\icon.ico cmd.py

rd build /s/q
rd cmd.build /s/q
rd cmd.dist /s/q
rd cmd.onefile-build /s/q
del cmd.cmd
move cmd.exe OrbitalCmd.exe
move dist\Orbital.exe Orbital.exe
rd dist /s/q
