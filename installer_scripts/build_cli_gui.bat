@echo off
echo Building EXEs with embedded icon...

REM CLI version
pyinstaller --onefile --icon=assets\logo.ico --name heic2jpeg src\heic2jpeg.py

REM GUI version
pyinstaller --onefile --windowed --icon=assets\logo.ico --name heic2jpeg_gui src\heic2jpeg_gui.py

REM Launcher
pyinstaller --onefile --windowed --icon=assets\logo.ico --name launcher src\launcher.py

echo Build complete!
pause
