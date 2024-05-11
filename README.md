# OBS WayKey

Python script for setting up OBS global keybinds under wayland

## Requirements

-   [OBS Studio](https://obsproject.com/)
-   [OBS Websocket v5 Plugin](https://github.com/obsproject/obs-websocket/releases/tag/5.0.0)
    -   ATTENTION: For OBS version 28 and above Websocket plugin is included by default. If you run an older version it must be installed manually.
-   Python 3.9 or greater

# Install and Setup

## Install

I recommend installing via [pipx](https://github.com/pypa/pipx)
**ATTENTION:** This package is currently not up on pypi so this command won't work

```
pipx install obs-waykey
```

If you want a specific version you can grab the `.vhl` from the [releases page](https://github.com/PolyCatDev/obs-waykey/releases) and install it with pipx

```
pipx install <file-name>
```

## Setup

ATTENTION: WebScoket authentication must be disabled for this script to work.

You can find it under `Tools > WebScoket Server Settings > Enable Authentication`.

1. Go to your Desktop settings (or WM config file)
2. Go to where you configure keybinds
3. Add a new custom keybind
4. Name it what u want
5. Use the command `obs-waykey <toggle>`
6. Set ur keybind

### Here's how mine looks

![my keybind](https://github.com/PolyCatDev/obs-waykey/blob/main/.github/toggle-rec-config.png)

## Toggles

1. `toggle-rec`
2. `toggle-rec-pause`

# Build from source

ATTENTION: This project was built with [poetry](https://python-poetry.org/) in mind.

1. Clone the repo

```
git clone https://github.com/PolyCatDev/obs-waykey.git && \
cd obs-waykey
```

2. Setup enviroment

```
python3 -m venv .venv && \
source .venv/bin/activate
```

3. Install dependencies

```
pip install poetry && \
poetry install
```

4. Build the package

```
poetry build
```

# To do

-   [ ] Add more toggles
-   [ ] Password Support
-   [ ] Alternative IP support
-   [ ] Alternative port support
