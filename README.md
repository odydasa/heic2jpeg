[![CI](https://github.com/odydasa/heic2jpeg/actions/workflows/python-package.yml/badge.svg)](https://github.com/odydasa/heic2jpeg/actions/workflows/python-package.yml)

🔄 Convert HEIC to JPEG using Python with full-featured CLI, GUI, and EXE — powered by Pillow and Pillow-HEIF.

# heic2jpeg

**heic2jpeg** is a Python-based tool to convert `.heic` images to `.jpg` (JPEG format).  
It includes timestamp preservation, optional source deletion, and output folder selection.

---

## 📦 Package Contents

- `heic2jpeg.py` – CLI version
- `heic2jpeg_gui.py` – GUI version (Tkinter)
- `launcher.py` – simple interface to choose between CLI and GUI
- `README.md` – this documentation
- `docs/` – HTML documentation (MkDocs)
- `.github/workflows/` – CI configuration
- `assets/logo.png` – icon and logo
- `installer_scripts/` – scripts for building `.exe` versions and installer

---

## ✅ Features

- Convert `.heic` → `.jpg` (JPEG)
- Preserve original timestamps (modified & accessed)
- Force overwrite with `-f`
- Remove original `.heic` with `-r`
- Show file info with `-v`
- Specify output folder with `--output <folder>`

---

## 🖥️ How to Run

### 1. CLI
```bash
python src/heic2jpeg.py [options] <file|folder|*.heic>
```

Example:
```bash
python src/heic2jpeg.py -rfv --output out/ *.heic
```

### 2. GUI
```bash
python src/heic2jpeg_gui.py
```

### 3. Launcher
```bash
python src/launcher.py
```

---

## 🔧 Installation & Dependencies

Requires Python 3.8+

Install dependencies manually:
```bash
pip install pillow pillow-heif
```

---

## 🛠️ Build EXE Versions

Make sure `pyinstaller` is installed:
```bash
pip install pyinstaller
```

Then run:
```bash
pyinstaller --onefile --name heic2jpeg src/heic2jpeg.py
pyinstaller --onefile --windowed --name heic2jpeg_gui src/heic2jpeg_gui.py
pyinstaller --onefile --windowed --name launcher src/launcher.py
```

Output will be placed in the `dist/` folder.

---

## 🧩 Manual Dependency Installation (Cross-Platform)

### Windows (CMD/PowerShell):
```cmd
pip install pillow pillow-heif
```

### macOS:
```bash
brew install libheif
pip3 install pillow pillow-heif
```

### Ubuntu/Debian:
```bash
sudo apt install libheif1 libheif-dev
pip3 install pillow pillow-heif
```

### Fedora:
```bash
sudo dnf install libheif
pip install pillow pillow-heif
```

---

## 🪄 Automatic Dependency Installation

If running `heic2jpeg.py` directly, the script will:
- Check for `pillow` and `pillow-heif`
- Automatically install them via `pip` if missing

---

## 🪟 EXE Usage

If using the precompiled `.exe` versions:
- No Python or pip required
- All libraries are bundled inside
- Just run `heic2jpeg.exe` or `heic2jpeg_gui.exe`

---

## 🖼️ HEIC vs JPEG

**HEIC (High Efficiency Image Container)** offers:
- Smaller file size at higher quality
- Modern features like transparency and Live Photos

**JPEG** offers:
- Maximum compatibility
- Slightly larger file size
- No transparency support

This tool converts HEIC to JPEG while preserving:
- Timestamps (modified & accessed)
- Image fidelity within JPEG limits

---

## 📂 GitHub CLI Installation

```bash
gh repo clone odydasa/heic2jpeg
cd heic2jpeg
pip install -e .
```

Or:
```bash
pip install git+https://github.com/odydasa/heic2jpeg.git
```

---

## ⚠️ Disclaimer

This project, including all code, documentation, and structure, was fully generated using [ChatGPT](https://chat.openai.com) based on the user’s specifications.

Free to use under the MIT License.

---

## 🧠 Prompt to Reproduce
To regenerate this project using ChatGPT, see [`PROMPT.md`](PROMPT.md).


## Specification

See full specification in [PROMPT.md](PROMPT.md)
You are a professional software assistant. Please create a complete Python-based tool called **heic2jpeg** with the following specifications:

1. 🔁 **Function**: Convert `.heic` images to `.jpg` (JPEG format).

2. ✅ **Requirements**:
- Use `pillow` and `pillow-heif` for image handling.
- Ensure compatibility across Windows, macOS, and Linux.
- Auto-install any missing dependencies at runtime.
- Handle `.heic` files passed as:
  - Single file
  - Wildcard (e.g., `*.heic`)
  - Directory
- Retain original timestamps (created/modified/accessed).
- Validate HEIC by scanning for `ftyp` atom (128 bytes); fallback to `Image.open()` if needed.

3. 💡 **CLI Options**:
- `-f` → Force overwrite if `.jpg` exists.
- `-r` → Remove original `.heic` after conversion.
- `-v` → Verbose output for conversion logs.
- `--output <folder>` → Set destination folder for `.jpg` files.
- All options are combinable (e.g., `-rfv`).

4. 🖥️ **GUI Version**:
- Built with `Tkinter`.
- File/folder picker.
- Same functionality as CLI.

5. 🎨 Branding:
- Include a custom logo for the project (`logo.png`) in `assets/`.
- Convert and embed `logo.ico` as the application icon in all `.exe` builds (CLI, GUI, Launcher).
- Ensure the icon is visible in Windows Explorer and during installation.

6. 📦 **Packaging**:
- Generate `.exe` for CLI and GUI using `pyinstaller`.
- Embed `.ico` as application icon into `.exe`.
- Include Inno Setup script `.iss` for creating installer.
- Add launcher script to let users choose GUI or CLI.

7. 📂 **File structure**:
- `src/` → Contains all Python scripts.
- `docs/` → Documentation site (MkDocs or Sphinx).
- `assets/` → Logo and icons.
- `.github/workflows/` → GitHub Actions CI/CD for build.
- `installer_scripts/` → `.bat`, `.ps1`, `.iss` for Windows installer creation.
- `README.md` → In English, fully documents usage, setup, platforms.
- `setup.py`, `requirements.txt` → for packaging and PyPI.

8. 📚 **Documentation**:
- Include description of HEIC vs JPEG formats.
- Installation methods per OS (Linux/macOS/Windows/WSL).
- CLI usage and syntax.
- GUI usage.
- Manual vs automatic dependency install.
- Add disclaimer that all code was generated via ChatGPT.

9. 📎 **Bonus**:
- Add detailed comments in all code.
- Add a final summary of converted/skipped/failed files.
- Include this prompt inside the `README.md`.

10. ➡️ Please generate the full codebase in English, package all of it into a `.zip`, and ensure the structure is ready for GitHub sync.
```
