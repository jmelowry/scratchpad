# scratchpad (`sp`)

A tiny CLI tool for daily markdown notes. Saves timestamped entries to `~/scratchpad/YYYY-MM-DD.md` (default) or `$SCRATCHPAD_DIR`.

## Install

```bash
git clone https://github.com/jmelowry/scratchpad.py.git
cd scratchpad.py
```

Make it easy to run:

### bash
```bash
echo "alias sp='python3 $(pwd)/bin/main.py'" >> ~/.bash_profile
source ~/.bash_profile
```

### zsh
```bash
echo "alias sp='python3 $(pwd)/bin/main.py'" >> ~/.zshrc
source ~/.zshrc
```

Or just run it directly:

```bash
python3 $(pwd)/bin/main.py note
```

## Usage

```bash
sp quick note
sp               # opens today’s file in your $EDITOR
```

