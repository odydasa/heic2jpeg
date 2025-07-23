"""
heic2jpeg - Convert HEIC to JPEG (CLI and GUI)

Author: Generated with ChatGPT for odydasa/heic2jpeg
License: MIT
MIT License (c) 2025 OdyDasa
This tool and documentation were generated and assembled using ChatGPT.

Uses pillow-heif (no C compiler needed)
GUI: HEIC2JPEG GUI using Tkinter
"""

import os

import sys

import tkinter as tk

from tkinter import filedialog, messagebox, ttk, scrolledtext

import subprocess

import importlib

# Auto-install required packages

def install_if_missing(package, pip_name=None):
    pip_name = pip_name or package
    try:
        importlib.import_module(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", pip_name])

install_if_missing("PIL", "pillow")
install_if_missing("pillow_heif", "pillow-heif")


from PIL import Image

import pillow_heif
pillow_heif.register_heif_opener()

# Determine if file is HEIC based on header

def is_probably_heic(file_path):
    try:
        with open(file_path, 'rb') as f:
            header = f.read(128)
            return b'ftyp' in header
    except:
        return False

# Convert a single file

def convert_heic_to_jpg(input_path, output_dir, force=False, remove=False, log=None):
    base_name = os.path.splitext(os.path.basename(input_path))[0] + ".jpg"
    output_path = os.path.join(output_dir if output_dir else os.path.dirname(input_path), base_name)

    if os.path.exists(output_path) and not force:
        if log: log.insert(tk.END, f"Skipped (exists): {output_path}\n")
        return "skipped"

    try:
        if not is_probably_heic(input_path):
            raise ValueError("Not valid HEIC header. Trying fallback.")

        image = Image.open(input_path)
        image.save(output_path, format="JPEG")
    except Exception:
        try:
            image = Image.open(input_path)
            image.save(output_path, format="JPEG")
        except Exception as e:
            if log: log.insert(tk.END, f"[ERROR] Failed: {input_path}\n")
            return "failed"

    try:
        stat = os.stat(input_path)
        os.utime(output_path, (stat.st_atime, stat.st_mtime))
    except:
        pass

    if remove:
        try: os.remove(input_path)
        except: pass

    if log: log.insert(tk.END, f"[✓] Converted: {output_path}\n")
    return "converted"

# Collect HEIC files from file/folder input

def collect_heic_files(paths):
    collected = []
    for path in paths:
        if os.path.isfile(path) and path.lower().endswith(".heic"):
            collected.append(path)
        elif os.path.isdir(path):
            for root, _, files in os.walk(path):
                for f in files:
                    if f.lower().endswith(".heic"):
                        collected.append(os.path.join(root, f))
    return collected


def select_files_or_folders():
    files = filedialog.askopenfilenames(filetypes=[("HEIC files", "*.heic")])
    folder = filedialog.askdirectory(title="Choose Folder")
    paths = list(files)
    if folder:
        paths.append(folder)
    return paths


def run_conversion():
    inputs = select_files_or_folders()
    if not inputs: return

    output_dir = None  # Use input file's folder as output

    force = force_var.get()
    remove = remove_var.get()
    verbose = verbose_var.get()

    log_text.config(state='normal')
    log_text.delete(1.0, tk.END)

    files = collect_heic_files(inputs)
    summary = {"converted": 0, "skipped": 0, "failed": 0}

    for f in files:
        result = convert_heic_to_jpg(f, output_dir, force, remove, log_text if verbose else None)
        if result in summary:
            summary[result] += 1

    if verbose:
        log_text.insert(tk.END, "\nSummary:\n")
        log_text.insert(tk.END, f"  ✓ Converted: {summary['converted']}\n")
        log_text.insert(tk.END, f"  → Skipped:   {summary['skipped']}\n")
        log_text.insert(tk.END, f"  ✗ Failed:    {summary['failed']}\n")

    log_text.config(state='disabled')

    messagebox.showinfo("Conversion Summary",
                        f"✓ Converted: {summary['converted']}\n→ Skipped: {summary['skipped']}\n✗ Failed: {summary['failed']}")

# GUI Layout
root = tk.Tk()
root.title("HEIC2JPEG GUI Converter")

try:
    icon_path = os.path.join(os.path.dirname(__file__), "..", "assets", "logo.ico")
    root.iconbitmap(icon_path)
except:
    pass

frame = ttk.Frame(root, padding=20)
frame.grid(row=0, column=0, sticky="nsew")

ttk.Label(frame, text="HEIC to JPEG Converter", font=("Arial", 16)).grid(column=0, row=0, columnspan=4, pady=10)

ttk.Button(frame, text="Select HEIC Files / Folder", command=run_conversion).grid(column=0, row=1, columnspan=4, pady=5)

force_var = tk.BooleanVar(value=True)
remove_var = tk.BooleanVar(value=False)
verbose_var = tk.BooleanVar(value=True)

ttk.Checkbutton(frame, text="Force overwrite", variable=force_var).grid(column=0, row=2, sticky="w")
ttk.Checkbutton(frame, text="Remove originals", variable=remove_var).grid(column=1, row=2, sticky="w")
ttk.Checkbutton(frame, text="Verbose summary", variable=verbose_var).grid(column=2, row=2, sticky="w")

log_text = scrolledtext.ScrolledText(frame, width=80, height=18, state='disabled')
log_text.grid(column=0, row=3, columnspan=4, pady=10)

root.mainloop()

def main():
    root.mainloop()

