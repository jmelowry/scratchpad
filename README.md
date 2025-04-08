# scratchpad (`sp`)

A tiny CLI tool for daily markdown notes. Saves timestamped entries to `~/scratchpad/YYYY-MM-DD.md`.

## Usage

```bash
sp "quick note"
sp               # opens today’s file in your $EDITOR
```

## Install

```bash
git clone https://github.com/jmelowry/scratchpad.py.git
```

Make it easy to run:

### bash
```bash
echo "alias sp='~/scratchpad.py/bin/sp'" >> ~/.bash_profile
source ~/.bash_profile
```

### zsh
```bash
echo "alias sp='~/scratchpad.py/bin/sp'" >> ~/.zshrc
source ~/.zshrc
```

Or just run it directly:

```bash
~/scratchpad.py/bin/sp "note"
```


