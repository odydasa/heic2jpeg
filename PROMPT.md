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
