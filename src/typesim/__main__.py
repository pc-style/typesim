"""
Main CLI entry point for typesim.
Handles text input, countdown, and integration.
"""

import sys
import time
from rich.console import Console
from rich.panel import Panel
from rich import box
from . import keyboard_ctrl
from . import typing_engine
from . import shortcuts
from . import tui
from . import config_manager

console = Console()

def draw_banner():
    """Draw a nice banner."""
    console.print("\n" + "=" * 50)
    console.print("  [bold cyan]REALISTIC TYPING SIMULATOR[/bold cyan]")
    console.print("=" * 50 + "\n")

def get_text_input() -> str:
    """Get multiline text input from user."""
    console.print("[cyan]Paste or type your text (press Ctrl+D or empty line + Enter to finish):[/cyan]")
    console.print("-" * 50)
    
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
    
    console.print(f"\n[cyan]Starting in {seconds} seconds... Switch to your target app now![/cyan]")
    console.print("[dim](Keyboard shortcuts: F9=pause, Ctrl+/Ctrl-=speed, Esc=stop)[/dim]\n")
    
    for i in range(seconds, 0, -1):
        console.print(f"  [yellow]{i}...[/yellow]")
        time.sleep(1)
        if shortcuts.is_stopped():
            return False
    
    console.print("  [bold green]GO![/bold green]\n")
    time.sleep(0.3)  # brief pause before typing starts
    return True

def show_shortcuts_help():
    """Show keyboard shortcuts help."""
    table = Panel(
        "[cyan]F9[/cyan] = Pause/Resume\n"
        "[cyan]Ctrl + +[/cyan] = Speed Up\n"
        "[cyan]Ctrl + -[/cyan] = Speed Down\n"
        "[cyan]Esc[/cyan] = Stop",
        title="[bold cyan]Keyboard Shortcuts[/bold cyan]",
        border_style="cyan"
    )
    console.print(table)

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
        console.print("\n[dim]Typing started...[/dim]\n")
        
        # start typing
        typing_engine.type_text_realistic(text)
        
        if shortcuts.is_stopped():
            console.print("\n\n[red]Stopped by user.[/red]")
        else:
            console.print("\n\n[green]Done! Finished typing.[/green]")
    
    except KeyboardInterrupt:
        console.print("\n\n[yellow]Interrupted.[/yellow]")
        shortcuts.request_stop()
    finally:
        shortcuts.stop_listener()

def main():
    """Main entry point."""
    draw_banner()
    
    # reset stop flag
    keyboard_ctrl.set_stop_flag(False)
    shortcuts.reset()
    
    cfg = config_manager.get_config_manager()
    
    while True:
        choice = tui.show_main_menu()
        
        if choice == "q":
            console.print("\n[cyan]Goodbye![/cyan]\n")
            break
        
        elif choice == "1":  # Start Typing
            console.clear()
            draw_banner()
            
            # get text to type
            text = get_text_input()
            
            if not text:
                console.print("[red]No text provided.[/red]")
                input("\nPress Enter to continue...")
                continue
            
            console.print(f"\n[cyan]Text length:[/cyan] {len(text)} characters")
            console.print("[cyan]Press Enter to start countdown, or Ctrl+C to cancel...[/cyan]")
            
            try:
                input()
            except KeyboardInterrupt:
                console.print("\n[yellow]Cancelled.[/yellow]")
                continue
            
            # countdown
            if not countdown():
                console.print("[yellow]Stopped before starting.[/yellow]")
                continue
            
            # start typing!
            type_text(text)
            
            input("\nPress Enter to continue...")
        
        elif choice == "2":  # Settings
            tui.show_settings_menu()
        
        elif choice == "p":  # Presets
            tui.show_presets_menu()
        
        elif choice == "3":  # Load from File
            console.clear()
            draw_banner()
            text = tui.get_file_path()
            
            if text:
                console.print(f"\n[green]Loaded {len(text)} characters from file[/green]")
                console.print("[cyan]Press Enter to start countdown, or Ctrl+C to cancel...[/cyan]")
                
                try:
                    input()
                except KeyboardInterrupt:
                    console.print("\n[yellow]Cancelled.[/yellow]")
                    continue
                
                if countdown():
                    type_text(text)
                
                input("\nPress Enter to continue...")
            else:
                input("\nPress Enter to continue...")
        
        elif choice == "e":  # Export Config
            tui.export_config_menu()
        
        elif choice == "i":  # Import Config
            tui.import_config_menu()
        
        elif choice == "4":  # Reset to Defaults
            from rich.prompt import Confirm
            if Confirm.ask("[yellow]Reset all settings to defaults?[/yellow]"):
                cfg.reset_to_defaults()
                console.print("[green]Settings reset to defaults[/green]")
                input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
