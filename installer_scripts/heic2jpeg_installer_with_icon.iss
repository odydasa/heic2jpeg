[Setup]
AppName=HEIC2JPEG
AppVersion=1.0
DefaultDirName={pf}\HEIC2JPEG
DefaultGroupName=HEIC2JPEG
UninstallDisplayIcon={app}\heic2jpeg_gui.exe
OutputDir=dist
OutputBaseFilename=heic2jpeg_installer
Compression=lzma
SolidCompression=yes
SetupIconFile=assets\logo.ico

[Files]
Source: "dist\heic2jpeg.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\heic2jpeg_gui.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\HEIC2JPEG (CLI)"; Filename: "{app}\heic2jpeg.exe"; IconFilename: "{app}\heic2jpeg.exe"
Name: "{group}\HEIC2JPEG (GUI)"; Filename: "{app}\heic2jpeg_gui.exe"; IconFilename: "{app}\heic2jpeg_gui.exe"
