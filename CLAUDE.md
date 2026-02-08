# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Single-script Python tool that batch-converts HEIC/HEIF images to JPG. All logic is in `heic_converter.py`. Comments and UI strings are in Traditional Chinese (zh-TW).

## Setup and Running

```bash
# Activate the venv (Python 3.10)
source .venv/bin/activate

# Run the converter
python heic_converter.py <input_dir>
python heic_converter.py <input_dir> -o <output_dir>
python heic_converter.py <input_dir> -q 90 --no-recursive
```

Dependencies: `pillow`, `pillow_heif`, `tqdm` (all installed in `.venv`).

## Architecture

The script has three layers:
- `convert_heic_to_jpg()` — converts a single file (opens HEIC via pillow_heif's registered opener, converts to RGB, saves as JPEG)
- `find_heic_files()` — recursively globs a directory for `.heic`/`.heif` files
- `batch_convert()` — orchestrates the batch process with progress bar (tqdm), tracks success/failure counts
- `main()` — argparse CLI entry point

`pillow_heif.register_heif_opener()` is called at module level to register HEIF format support with Pillow.

## Conventions

- The `input/` and `output/` directories are working directories for image files — do not commit image data to them.
- When `--output` is not specified, JPG files are created alongside the original HEIC files. When specified, the relative directory structure from the input is preserved in the output.
