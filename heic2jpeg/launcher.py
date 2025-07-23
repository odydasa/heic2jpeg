"""
heic2jpeg - Convert HEIC to JPEG (CLI and GUI)

Author: Generated with ChatGPT for odydasa/heic2jpeg
License: MIT
MIT License (c) 2025 OdyDasa
This tool and documentation were generated and assembled using ChatGPT.

Uses pillow-heif (no C compiler needed)
Launcher: Lets user choose between CLI and GUI
"""

import subprocess
import tkinter as tk

def run_cli():
    subprocess.run(["python", "src/heic2jpeg.py", "--help"])


def run_gui():
    subprocess.run(["python", "src/heic2jpeg_gui.py"])


root = tk.Tk()
root.title("HEIC2JPEG Launcher")
frame = tk.Frame(root, padx=30, pady=30)
frame.pack()

label = tk.Label(frame, text="Choose Mode to Run", font=("Arial", 14))
label.pack(pady=10)

tk.Button(frame, text="Run CLI (Command Line)", command=run_cli).pack(pady=5)
tk.Button(frame, text="Run GUI (Graphical)", command=run_gui).pack(pady=5)

root.mainloop()

