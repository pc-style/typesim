"""
Keyboard control using pynput.
Handles actual keypress simulation.
"""

from pynput import keyboard
from pynput.keyboard import Key, Controller
import time

# global controller instance
_kb_controller = None

def get_controller():
    """Get or create keyboard controller."""
    global _kb_controller
    if _kb_controller is None:
        _kb_controller = Controller()
    return _kb_controller

def type_char(char: str):
    """Type a single character."""
    ctrl = get_controller()
    ctrl.type(char)

def press_backspace(count: int = 1):
    """Press backspace N times."""
    ctrl = get_controller()
    for _ in range(count):
        ctrl.press(Key.backspace)
        ctrl.release(Key.backspace)
        time.sleep(0.01)  # small delay between backspaces

def press_enter():
    """Press Enter key."""
    ctrl = get_controller()
    ctrl.press(Key.enter)
    ctrl.release(Key.enter)

def press_space():
    """Press Space key."""
    ctrl = get_controller()
    ctrl.press(Key.space)
    ctrl.release(Key.space)

# global flag for emergency stop
_stop_requested = False

def set_stop_flag(value: bool):
    """Set the emergency stop flag."""
    global _stop_requested
    _stop_requested = value

def is_stopped() -> bool:
    """Check if stop was requested."""
    return _stop_requested

def setup_escape_listener():
    """Set up listener for Esc key to stop typing."""
    def on_press(key):
        try:
            if key == Key.esc:
                set_stop_flag(True)
                return False  # stop listener
        except AttributeError:
            pass
        return True  # continue listening for other keys
    
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    return listener

