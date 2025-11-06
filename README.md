# Realistic Typing Simulator

A Python tool that simulates realistic human typing behavior - complete with typos, corrections, thinking pauses, and mid-sentence edits. Perfect for making your typing look more natural and human-like.

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Features

- **Realistic typos**: Randomly hits neighboring keys on QWERTY keyboard
- **Automatic corrections**: Backspaces and fixes typos naturally
- **Variable typing speed**: Randomized delays between keystrokes
- **Thinking pauses**: Longer pauses at sentence boundaries, commas, and paragraphs
- **Mid-sentence edits**: Goes back to change words, insert phrases, or improve text
- **Sentence rephrasing**: Types rephrased versions then changes back (AI-powered)
- **Keyboard shortcuts**: Pause, speed control, stop
- **TUI Settings Menu**: Configure all behaviors through a beautiful interface
- **File loading**: Read text from files
- **AI integration**: Optional Gemini API for smarter word suggestions and rephrasing
- **Emergency stop**: Press Esc anytime to stop typing

## Installation

### Quick Install (from GitHub)

```bash
# Install directly from GitHub using uv
uv tool install git+https://github.com/pc-style/typesim.git
```

### Development Installation

This project uses [UV](https://github.com/astral-sh/uv) for dependency management.

```bash
# Clone the repository
git clone https://github.com/pc-style/typesim.git
cd typesim

# Install dependencies
uv sync

# Or install in development mode
uv pip install -e .
```

## Setup

1. Get a Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey) (optional, for AI features)
2. Set it as an environment variable:
   ```bash
   export GEMINI_API_KEY="your-api-key-here"
   ```
3. Install dependencies:
   ```bash
   uv sync
   ```

## Usage

Run the simulator:

```bash
# If installed via uv tool install
typesim

# If running from source
uv run typesim
```

### Main Menu

The TUI provides a main menu with options:
1. **Start Typing** - Enter text and start typing simulation
2. **Settings** - Configure all typing behaviors
3. **Load from File** - Load text from a file
4. **Reset to Defaults** - Reset all settings

### Keyboard Shortcuts (During Typing)

- **Space** - Pause/Resume typing
- **+** - Increase typing speed
- **-** - Decrease typing speed
- **Esc** - Stop typing completely

### Workflow

1. Run the command
2. Choose option from main menu
3. Enter text (or load from file)
4. Press Enter to start the countdown
5. **Switch to your target app** (text editor, chat, etc.)
6. Watch the realistic typing happen!
7. Use keyboard shortcuts to control typing

## Configuration

All settings can be configured through the TUI Settings Menu (option 2):

### Behavior Probabilities
- **Typo Probability**: Chance of making a typo per character (0-50%)
- **Edit Probability**: Chance to go back and edit something (0-100%)
- **Rephrase Probability**: Chance to rephrase entire sentences (0-100%)

### Timing Settings
- **Base Delay**: Normal typing speed range (min/max in milliseconds)
- **Thinking Pause**: Pause duration for thinking (min/max in milliseconds)
- **Sentence Pause**: Pause at sentence ends (min/max in milliseconds)
- **Comma Pause**: Pause at commas (min/max in milliseconds)

### Other Settings
- **Use AI**: Toggle Gemini API features (synonyms, rephrasing)
- **Countdown Seconds**: Countdown duration before typing starts
- **Speed Multiplier**: Base typing speed multiplier (0.1x to 5.0x)

### Configuration File

Settings are saved to `~/.typesim/config.yaml` and persist between sessions.

## Requirements

- Python 3.12+
- pynput (for keyboard control)
- google-genai (for Gemini API integration, optional)
- rich (for TUI)
- pyyaml (for config persistence)

## Notes

- Make sure you have time to switch to your target app during the countdown
- The simulator types into whatever window is active after the countdown
- On macOS, you may need to grant accessibility permissions for keyboard control
- If Gemini API is unavailable or disabled, the app falls back to hardcoded alternatives
- Configuration is saved automatically when you exit the settings menu

## Examples

### Basic Usage
```bash
typesim
# Choose option 1
# Paste your text
# Press Enter
# Switch to target app
```

### Load from File
```bash
typesim
# Choose option 3
# Enter file path: /path/to/text.txt
# Press Enter
# Switch to target app
```

### Adjust Settings
```bash
typesim
# Choose option 2
# Edit any setting
# Press 'b' to go back (saves automatically)
```
