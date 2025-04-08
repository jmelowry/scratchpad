import os
import tempfile
from pathlib import Path
from bin import main

def test_get_scratchpad_dir_defaults_to_home(monkeypatch):
    monkeypatch.delenv("SCRATCHPAD_DIR", raising=False)
    expected = Path.home() / "scratchpad"
    assert main.get_scratchpad_dir() == expected

def test_get_scratchpad_dir_uses_env(monkeypatch):
    monkeypatch.setenv("SCRATCHPAD_DIR", "/tmp/foo")
    assert main.get_scratchpad_dir() == Path("/tmp/foo")

def test_get_today_file_creates_file(tmp_path):
    file = main.get_today_file(tmp_path)
    assert file.parent.exists()
    assert file.name.endswith(".md")

def test_append_note_writes_to_file(tmp_path):
    f = tmp_path / "test.md"
    main.append_note(f, "hello world")
    content = f.read_text()
    assert "hello world" in content
    assert "[" in content  # timestamp bracket

def test_editor_default(monkeypatch):
    monkeypatch.delenv("EDITOR", raising=False)
    assert main.open_in_editor.__code__.co_argcount == 1
