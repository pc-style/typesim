"""
Keyboard shortcuts handler for typing control.
"""

from pynput import keyboard
from pynput.keyboard import Key
import threading

# global state
_paused = False
_speed_multiplier = 1.0
_stop_requested = False
_listener = None

def is_paused() -> bool:
    """Check if typing is paused."""
    return _paused

def toggle_pause():
    """Toggle pause state."""
    global _paused
    _paused = not _paused

def set_paused(value: bool):
    """Set pause state."""
    global _paused
    _paused = value

def get_speed_multiplier() -> float:
    """Get current speed multiplier."""
    return _speed_multiplier

def set_speed_multiplier(value: float):
    """Set speed multiplier (0.1 to 5.0)."""
    global _speed_multiplier
    _speed_multiplier = max(0.1, min(5.0, value))

def increase_speed(amount: float = 0.1):
    """Increase speed."""
    set_speed_multiplier(_speed_multiplier + amount)

def decrease_speed(amount: float = 0.1):
    """Decrease speed."""
    set_speed_multiplier(_speed_multiplier - amount)

def request_stop():
    """Request stop."""
    global _stop_requested
    _stop_requested = True

def is_stopped() -> bool:
    """Check if stop requested."""
    return _stop_requested

def reset():
    """Reset all state."""
    global _paused, _speed_multiplier, _stop_requested
    _paused = False
    _speed_multiplier = 1.0
    _stop_requested = False

def setup_shortcuts_listener():
    """Set up keyboard shortcuts listener."""
    global _listener
    
    # track pressed keys for combinations
    _ctrl_pressed = False
    _alt_pressed = False
    
    def on_press(key):
        nonlocal _ctrl_pressed, _alt_pressed
        try:
            # Track modifier keys
            if key in (Key.ctrl_l, Key.ctrl_r, Key.cmd, Key.cmd_r):
                _ctrl_pressed = True
                return True
            
            if key in (Key.alt_l, Key.alt_r):
                _alt_pressed = True
                return True
            
            # F9 = pause/resume (unlikely to be typed in text)
            if key == Key.f9:
                toggle_pause()
                return True
            
            # Esc = stop
            if key == Key.esc:
                request_stop()
                return False  # stop listener
            
            # Ctrl + = or Ctrl + + = speed up
            if _ctrl_pressed and hasattr(key, 'char') and key.char in ('+', '='):
                increase_speed(0.1)
                return True
            
            # Ctrl + - or Ctrl + _ = speed down
            if _ctrl_pressed and hasattr(key, 'char') and key.char in ('-', '_'):
                decrease_speed(0.1)
                return True
            
        except AttributeError:
            # handle special keys
            pass
        
        return True
    
    def on_release(key):
        nonlocal _ctrl_pressed, _alt_pressed
        try:
            if key in (Key.ctrl_l, Key.ctrl_r, Key.cmd, Key.cmd_r):
                _ctrl_pressed = False
            if key in (Key.alt_l, Key.alt_r):
                _alt_pressed = False
        except:
            pass
    
    _listener = keyboard.Listener(on_press=on_press, on_release=on_release, suppress=False)
    _listener.start()
    return _listener

def stop_listener():
    """Stop the shortcuts listener."""
    global _listener
    if _listener:
        _listener.stop()
        _listener = None

