#!/usr/bin/env python3
import os, sys, subprocess
from datetime import datetime
from pathlib import Path
from typing import Optional

def get_scratchpad_dir() -> Path:
    return Path(os.environ.get("SCRATCHPAD_DIR", Path.home() / "scratchpad"))

def get_today_file(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path / (datetime.today().strftime("%Y-%m-%d") + ".md")

def append_note(file: Path, note: str) -> None:
    timestamp = datetime.now().strftime("%H:%M")
    with file.open("a") as f:
        f.write(f"\n[{timestamp}] {note.strip()}\n")

def open_in_editor(file: Path) -> None:
    editor = os.environ.get("EDITOR", "vim")
    subprocess.call([editor, str(file)])

def main() -> None:
    path = get_scratchpad_dir()
    file = get_today_file(path)
    if len(sys.argv) > 1:
        append_note(file, " ".join(sys.argv[1:]))
    else:
        open_in_editor(file)

if __name__ == "__main__":
    main()