"""
heic2jpeg - Convert HEIC to JPEG (CLI and GUI)

Author: Generated with ChatGPT for odydasa/heic2jpeg
License: MIT
MIT License (c) 2025 OdyDasa
This tool and documentation were generated and assembled using ChatGPT.

Uses pillow-heif (no C compiler needed)
"""

import argparse
import glob
import importlib
import os
import subprocess
import sys
from PIL import Image
import pillow_heif


# Auto-install required dependencies
def install_if_missing(package, pip_name=None):
    pip_name = pip_name or package
    try:
        importlib.import_module(package)
    except ImportError:
        print(f"[INFO] Installing: {pip_name}")
        subprocess.check_call([sys.executable, "-m", "pip", "install", pip_name])


install_if_missing("PIL", "pillow")
install_if_missing("pillow_heif", "pillow-heif")

pillow_heif.register_heif_opener()


# Check if file is likely a HEIC using FTYP header atom
def is_probably_heic(file_path):
    try:
        with open(file_path, 'rb') as f:
            header = f.read(128)
            return b'ftypheic' in header or b'ftypmif1' in header or b'ftyp' in header
    except Exception:
        return False


# Convert a single HEIC file
def convert_heic_to_jpg(input_path, output_dir=None, force=False, remove=False, verbose=False):
    base_name = os.path.splitext(os.path.basename(input_path))[0] + ".jpg"
    output_path = os.path.join(output_dir if output_dir else os.path.dirname(input_path), base_name)

    if os.path.exists(output_path) and not force:
        if verbose:
            print(f"[i] Skipped (exists): {output_path}")
        return "skipped"

    try:
        if not is_probably_heic(input_path):
            raise ValueError("FTYP signature not found. Trying fallback.")

        image = Image.open(input_path)
        image.save(output_path, format="JPEG")
    except Exception:
        try:
            if verbose:
                print(f"[!] Fallback open: {input_path}")
            image = Image.open(input_path)
            image.save(output_path, format="JPEG")
        except Exception as fallback_error:
            print(f"[ERROR] Failed to convert {input_path}: {fallback_error}")
            return "failed"

    try:
        stat = os.stat(input_path)
        os.utime(output_path, (stat.st_atime, stat.st_mtime))
    except Exception:
        pass

    if verbose:
        print(f"[✓] Converted: {input_path} → {output_path}")

    if remove:
        try:
            os.remove(input_path)
        except Exception:
            pass

    return "converted"


# Collect .heic files from single file, wildcard or directory
def collect_heic_files(paths):
    collected = []
    for path in paths:
        if os.path.isfile(path) and path.lower().endswith(".heic"):
            collected.append(path)
        elif "*" in path:
            collected.extend(glob.glob(path))
        elif os.path.isdir(path):
            for root, _, files in os.walk(path):
                for f in files:
                    if f.lower().endswith(".heic"):
                        collected.append(os.path.join(root, f))
    return collected


# Entry point for CLI usage
def main():
    parser = argparse.ArgumentParser(description="Convert HEIC images to JPEG")
    parser.add_argument("inputs", nargs="*", help="HEIC files, wildcard, or folders")
    parser.add_argument("-f", "--force", action="store_true", help="Force overwrite if JPG exists")
    parser.add_argument("-r", "--remove", action="store_true", help="Remove original HEIC after conversion")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
    parser.add_argument("--output", type=str, help="Output folder for converted JPEGs")

    args = parser.parse_args()

    heic_files = collect_heic_files(args.inputs)
    if not heic_files:
        print("[i] No input files specified. Using current working directory.")
        heic_files = collect_heic_files([os.getcwd()])
        if not heic_files:
            print("[!] No HEIC files found.")
            return

    total = {"converted": 0, "skipped": 0, "failed": 0}

    for f in heic_files:
        result = convert_heic_to_jpg(
            f,
            output_dir=args.output,
            force=args.force,
            remove=args.remove,
            verbose=args.verbose
        )
        if result in total:
            total[result] += 1

    print("\nSummary:")
    print(f"  ✓ Converted: {total['converted']}")
    print(f"  → Skipped:   {total['skipped']}")
    print(f"  ✗ Failed:    {total['failed']}")


if __name__ == "__main__":
    main()
