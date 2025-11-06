"""
Configuration for realistic typing simulation.
Now uses config_manager for dynamic configuration.
"""

import random
from . import config_manager

def _get_cfg(key: str, default):
    """Get config value from manager."""
    return config_manager.get_config_manager().get(key, default)

# Typo probability - chance of making a typo per character
def TYPO_PROBABILITY():
    return _get_cfg('typo_probability', 0.08)

# Speed settings (in milliseconds)
def BASE_DELAY_MIN():
    return _get_cfg('base_delay_min', 30)

def BASE_DELAY_MAX():
    return _get_cfg('base_delay_max', 150)

def THINKING_PAUSE_MIN():
    return _get_cfg('thinking_pause_min', 500)

def THINKING_PAUSE_MAX():
    return _get_cfg('thinking_pause_max', 2000)

def SENTENCE_PAUSE_MIN():
    return _get_cfg('sentence_pause_min', 800)

def SENTENCE_PAUSE_MAX():
    return _get_cfg('sentence_pause_max', 2500)

def COMMA_PAUSE_MIN():
    return _get_cfg('comma_pause_min', 200)

def COMMA_PAUSE_MAX():
    return _get_cfg('comma_pause_max', 600)

# Edit/revision probability - chance to go back and edit something
def EDIT_PROBABILITY():
    return _get_cfg('edit_probability', 0.18)

def SENTENCE_REPHRASE_PROBABILITY():
    return _get_cfg('sentence_rephrase_probability', 0.30)

def USE_AI():
    return _get_cfg('use_ai', True)

# QWERTY keyboard neighbor mappings for realistic typos
# maps each key to its neighboring keys that are easy to hit by mistake
KEYBOARD_NEIGHBORS = {
    'q': ['w', 'a'],
    'w': ['q', 'e', 'a', 's'],
    'e': ['w', 'r', 's', 'd'],
    'r': ['e', 't', 'd', 'f'],
    't': ['r', 'y', 'f', 'g'],
    'y': ['t', 'u', 'g', 'h'],
    'u': ['y', 'i', 'h', 'j'],
    'i': ['u', 'o', 'j', 'k'],
    'o': ['i', 'p', 'k', 'l'],
    'p': ['o', 'l'],
    'a': ['q', 'w', 's', 'z'],
    's': ['a', 'w', 'e', 'd', 'x', 'z'],
    'd': ['s', 'e', 'r', 'f', 'c', 'x'],
    'f': ['d', 'r', 't', 'g', 'v', 'c'],
    'g': ['f', 't', 'y', 'h', 'b', 'v'],
    'h': ['g', 'y', 'u', 'j', 'n', 'b'],
    'j': ['h', 'u', 'i', 'k', 'm', 'n'],
    'k': ['j', 'i', 'o', 'l', 'm'],
    'l': ['k', 'o', 'p'],
    'z': ['a', 's', 'x'],
    'x': ['z', 's', 'd', 'c'],
    'c': ['x', 'd', 'f', 'v'],
    'v': ['c', 'f', 'g', 'b'],
    'b': ['v', 'g', 'h', 'n'],
    'n': ['b', 'h', 'j', 'm'],
    'm': ['n', 'j', 'k'],
}

# uppercase versions too
for key in list(KEYBOARD_NEIGHBORS.keys()):
    KEYBOARD_NEIGHBORS[key.upper()] = [n.upper() for n in KEYBOARD_NEIGHBORS[key]]

def get_neighbor_key(char: str) -> str | None:
    """Get a random neighboring key for a typo, or None if no neighbors."""
    neighbors = KEYBOARD_NEIGHBORS.get(char.lower())
    if neighbors:
        neighbor = random.choice(neighbors)
        # preserve case
        return neighbor.upper() if char.isupper() else neighbor
    return None

def random_delay(min_ms: int, max_ms: int) -> float:
    """Get random delay in seconds."""
    return random.uniform(min_ms, max_ms) / 1000.0

def should_make_typo() -> bool:
    """Check if we should make a typo based on probability."""
    return random.random() < TYPO_PROBABILITY()

def should_edit() -> bool:
    """Check if we should go back and edit something."""
    return random.random() < EDIT_PROBABILITY()

def should_rephrase_sentence() -> bool:
    """Check if we should rephrase a sentence."""
    return random.random() < SENTENCE_REPHRASE_PROBABILITY()

