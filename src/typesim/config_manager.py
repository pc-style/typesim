"""
Configuration manager with save/load functionality.
"""

import os
import yaml
from pathlib import Path
from typing import Any

CONFIG_DIR = Path.home() / ".typesim"
CONFIG_FILE = CONFIG_DIR / "config.yaml"

# default config values
DEFAULT_CONFIG = {
    "typo_probability": 0.08,
    "edit_probability": 0.18,
    "sentence_rephrase_probability": 0.30,
    "base_delay_min": 30,
    "base_delay_max": 150,
    "thinking_pause_min": 500,
    "thinking_pause_max": 2000,
    "sentence_pause_min": 800,
    "sentence_pause_max": 2500,
    "comma_pause_min": 200,
    "comma_pause_max": 600,
    "use_ai": True,
    "countdown_seconds": 3,
    "speed_multiplier": 1.0,  # 1.0 = normal, 0.5 = slower, 2.0 = faster
}

# preset configurations
PRESETS = {
    "fast": {
        "name": "Fast Typing",
        "description": "Quick typing with minimal pauses",
        "typo_probability": 0.03,
        "edit_probability": 0.10,
        "sentence_rephrase_probability": 0.15,
        "base_delay_min": 20,
        "base_delay_max": 80,
        "thinking_pause_min": 200,
        "thinking_pause_max": 800,
        "sentence_pause_min": 400,
        "sentence_pause_max": 1200,
        "comma_pause_min": 100,
        "comma_pause_max": 300,
        "use_ai": False,
        "countdown_seconds": 3,
        "speed_multiplier": 1.5,
    },
    "slow": {
        "name": "Slow & Careful",
        "description": "Deliberate typing with lots of thinking",
        "typo_probability": 0.12,
        "edit_probability": 0.25,
        "sentence_rephrase_probability": 0.40,
        "base_delay_min": 50,
        "base_delay_max": 200,
        "thinking_pause_min": 1000,
        "thinking_pause_max": 3000,
        "sentence_pause_min": 1500,
        "sentence_pause_max": 4000,
        "comma_pause_min": 400,
        "comma_pause_max": 1000,
        "use_ai": True,
        "countdown_seconds": 3,
        "speed_multiplier": 0.7,
    },
    "realistic": {
        "name": "Realistic Human",
        "description": "Most human-like typing behavior",
        "typo_probability": 0.08,
        "edit_probability": 0.18,
        "sentence_rephrase_probability": 0.30,
        "base_delay_min": 30,
        "base_delay_max": 150,
        "thinking_pause_min": 500,
        "thinking_pause_max": 2000,
        "sentence_pause_min": 800,
        "sentence_pause_max": 2500,
        "comma_pause_min": 200,
        "comma_pause_max": 600,
        "use_ai": True,
        "countdown_seconds": 3,
        "speed_multiplier": 1.0,
    },
    "chaotic": {
        "name": "Chaotic",
        "description": "Lots of typos and corrections",
        "typo_probability": 0.20,
        "edit_probability": 0.35,
        "sentence_rephrase_probability": 0.50,
        "base_delay_min": 25,
        "base_delay_max": 180,
        "thinking_pause_min": 300,
        "thinking_pause_max": 1500,
        "sentence_pause_min": 600,
        "sentence_pause_max": 2000,
        "comma_pause_min": 150,
        "comma_pause_max": 500,
        "use_ai": True,
        "countdown_seconds": 3,
        "speed_multiplier": 1.2,
    },
    "professional": {
        "name": "Professional",
        "description": "Clean, fast typing with few mistakes",
        "typo_probability": 0.04,
        "edit_probability": 0.12,
        "sentence_rephrase_probability": 0.20,
        "base_delay_min": 25,
        "base_delay_max": 120,
        "thinking_pause_min": 400,
        "thinking_pause_max": 1500,
        "sentence_pause_min": 600,
        "sentence_pause_max": 2000,
        "comma_pause_min": 150,
        "comma_pause_max": 400,
        "use_ai": True,
        "countdown_seconds": 3,
        "speed_multiplier": 1.3,
    },
}

class ConfigManager:
    """Manages configuration with save/load."""
    
    def __init__(self):
        self.config = DEFAULT_CONFIG.copy()
        self.load()
    
    def load(self):
        """Load config from file."""
        if CONFIG_FILE.exists():
            try:
                with open(CONFIG_FILE, 'r') as f:
                    loaded = yaml.safe_load(f) or {}
                    self.config.update(loaded)
            except Exception as e:
                print(f"// error loading config: {e}")
    
    def save(self):
        """Save config to file."""
        try:
            CONFIG_DIR.mkdir(parents=True, exist_ok=True)
            with open(CONFIG_FILE, 'w') as f:
                yaml.dump(self.config, f, default_flow_style=False)
        except Exception as e:
            print(f"// error saving config: {e}")
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get config value."""
        return self.config.get(key, default)
    
    def set(self, key: str, value: Any):
        """Set config value."""
        self.config[key] = value
    
    def reset_to_defaults(self):
        """Reset all config to defaults."""
        self.config = DEFAULT_CONFIG.copy()
        self.save()
    
    def apply_preset(self, preset_name: str):
        """Apply a preset configuration."""
        if preset_name in PRESETS:
            preset = PRESETS[preset_name]
            # copy preset values (excluding name/description)
            for key, value in preset.items():
                if key not in ['name', 'description']:
                    self.config[key] = value
            self.save()
            return True
        return False
    
    def get_presets(self):
        """Get list of available presets."""
        return PRESETS
    
    def export_config(self, filepath: str):
        """Export current config to a file."""
        try:
            with open(filepath, 'w') as f:
                yaml.dump(self.config, f, default_flow_style=False)
            return True
        except Exception as e:
            print(f"// error exporting config: {e}")
            return False
    
    def import_config(self, filepath: str):
        """Import config from a file."""
        try:
            with open(filepath, 'r') as f:
                loaded = yaml.safe_load(f) or {}
                # validate keys
                valid_keys = set(DEFAULT_CONFIG.keys())
                loaded = {k: v for k, v in loaded.items() if k in valid_keys}
                self.config.update(loaded)
                self.save()
            return True
        except Exception as e:
            print(f"// error importing config: {e}")
            return False

# global instance
_config_manager = None

def get_config_manager() -> ConfigManager:
    """Get global config manager instance."""
    global _config_manager
    if _config_manager is None:
        _config_manager = ConfigManager()
    return _config_manager

