"""
Main CLI entry point for typesim.
Handles text input, countdown, and integration.
"""

import sys
import time
from rich.console import Console
from . import keyboard_ctrl
from . import typing_engine
from . import shortcuts
from . import tui
from . import config_manager

console = Console()

def get_text_input() -> str:
    """Get multiline text input from user."""
    console.print("\n  [dim]paste or type your text[/dim]")
    console.print("  [dim](empty line to finish)[/dim]\n")

    lines = []
    try:
        while True:
            line = input()
            if line == "" and lines:  # empty line after some input = done
                break
            lines.append(line)
    except EOFError:
        # Ctrl+D pressed
        pass

    text = "\n".join(lines)
    return text.strip()

def countdown(seconds: int = 3):
    """Show countdown before starting."""
    cfg = config_manager.get_config_manager()
    seconds = cfg.get('countdown_seconds', seconds)

    console.print(f"\n  [dim]starting in {seconds}s... switch to target app[/dim]\n")

    for i in range(seconds, 0, -1):
        console.print(f"  [yellow]{i}...[/yellow]")
        time.sleep(1)
        if shortcuts.is_stopped():
            return False

    console.print("  [green]go[/green]\n")
    time.sleep(0.3)  # brief pause before typing starts
    return True

def show_shortcuts_help():
    """Show keyboard shortcuts help."""
    console.print("  [dim]f9[/dim] pause/resume")
    console.print("  [dim]ctrl+[/dim] speed up")
    console.print("  [dim]ctrl-[/dim] speed down")
    console.print("  [dim]esc[/dim] stop")

def type_text(text: str):
    """Type text with all features enabled."""
    # reset shortcuts state
    shortcuts.reset()
    cfg = config_manager.get_config_manager()

    # set initial speed multiplier
    shortcuts.set_speed_multiplier(cfg.get('speed_multiplier', 1.0))

    # setup shortcuts listener
    listener = shortcuts.setup_shortcuts_listener()

    try:
        # show shortcuts help
        show_shortcuts_help()
        console.print()

        # start typing
        typing_engine.type_text_realistic(text)

        if shortcuts.is_stopped():
            console.print("\n\n  [red]stopped[/red]")
        else:
            console.print("\n\n  [green]done[/green]")

    except KeyboardInterrupt:
        console.print("\n\n  [yellow]interrupted[/yellow]")
        shortcuts.request_stop()
    finally:
        shortcuts.stop_listener()

def main():
    """Main entry point."""
    # reset stop flag
    keyboard_ctrl.set_stop_flag(False)
    shortcuts.reset()

    cfg = config_manager.get_config_manager()

    while True:
        choice = tui.show_main_menu()

        if choice == "q":
            console.print("\n  [dim]goodbye[/dim]\n")
            break

        elif choice == "1":  # Start Typing
            console.clear()

            # get text to type
            text = get_text_input()

            if not text:
                console.print("  [red]no text provided[/red]")
                input("\n  [dim]press enter...[/dim]")
                continue

            console.print(f"\n  [dim]{len(text)} characters[/dim]")
            console.print("  [dim]press enter to start...[/dim]")

            try:
                input()
            except KeyboardInterrupt:
                console.print("\n  [yellow]cancelled[/yellow]")
                continue

            # countdown
            if not countdown():
                console.print("  [yellow]stopped[/yellow]")
                continue

            # start typing!
            type_text(text)

            input("\n  [dim]press enter...[/dim]")

        elif choice == "2":  # Settings
            tui.show_settings_menu()

        elif choice == "p":  # Presets
            tui.show_presets_menu()

        elif choice == "3":  # Load from File
            console.clear()
            text = tui.get_file_path()

            if text:
                console.print(f"\n  [green]loaded {len(text)} characters[/green]")
                console.print("  [dim]press enter to start...[/dim]")

                try:
                    input()
                except KeyboardInterrupt:
                    console.print("\n  [yellow]cancelled[/yellow]")
                    continue

                if countdown():
                    type_text(text)

                input("\n  [dim]press enter...[/dim]")
            else:
                input("\n  [dim]press enter...[/dim]")

        elif choice == "e":  # Export Config
            tui.export_config_menu()

        elif choice == "i":  # Import Config
            tui.import_config_menu()

        elif choice == "4":  # Reset to Defaults
            from rich.prompt import Confirm
            if Confirm.ask("  [yellow]reset all settings to defaults?[/yellow]"):
                cfg.reset_to_defaults()
                console.print("  [green]reset to defaults[/green]")
                input("\n  [dim]press enter...[/dim]")

if __name__ == "__main__":
    main()
