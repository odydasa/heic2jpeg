Write-Host "Building EXEs with embedded icon..."

# CLI version
pyinstaller --onefile --icon=assets\logo.ico --name heic2jpeg src\heic2jpeg.py

# GUI version
pyinstaller --onefile --windowed --icon=assets\logo.ico --name heic2jpeg_gui src\heic2jpeg_gui.py

# Launcher
pyinstaller --onefile --windowed --icon=assets\logo.ico --name launcher src\launcher.py

Write-Host "Build complete!"
