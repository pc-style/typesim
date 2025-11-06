"""
Text User Interface for settings and configuration.
Uses inquirer for arrow-key navigation.
"""

import inquirer
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich import box
from typing import Callable, Any
from . import config_manager

console = Console()

def show_main_menu() -> str:
    """Show main menu with arrow key navigation."""
    console.clear()
    console.print("[bold cyan]Typesim Main Menu[/bold cyan]\n")
    
    questions = [
        inquirer.List(
            'choice',
            message="Select an option",
            choices=[
                ('Start Typing', '1'),
                ('Settings', '2'),
                ('Presets', 'p'),
                ('Load from File', '3'),
                ('Export Config', 'e'),
                ('Import Config', 'i'),
                ('Reset to Defaults', '4'),
                ('Quit', 'q'),
            ],
            carousel=True
        )
    ]
    
    answers = inquirer.prompt(questions)
    return answers['choice'] if answers else 'q'

def edit_number_setting(name: str, current: float, min_val: float = 0.0, max_val: float = 1.0, 
                        step: float = 0.01, is_percent: bool = False) -> float:
    """Edit a number setting."""
    console.clear()
    console.print(f"\n[cyan]{name}:[/cyan] [yellow]{current * 100 if is_percent else current}[/yellow]\n")
    
    while True:
        try:
            if is_percent:
                val_str = Prompt.ask(f"Enter new value ({min_val*100:.1f}-{max_val*100:.1f}%)", default=str(current * 100))
                val = float(val_str) / 100.0
            else:
                val_str = Prompt.ask(f"Enter new value ({min_val}-{max_val})", default=str(current))
                val = float(val_str)
            
            if min_val <= val <= max_val:
                return val
            else:
                console.print(f"[red]Value must be between {min_val} and {max_val}[/red]")
        except ValueError:
            console.print("[red]Invalid number[/red]")
        except KeyboardInterrupt:
            return current

def edit_int_setting(name: str, current: int, min_val: int = 0, max_val: int = 10000) -> int:
    """Edit an integer setting."""
    console.clear()
    console.print(f"\n[cyan]{name}:[/cyan] [yellow]{current}[/yellow]\n")
    
    while True:
        try:
            val_str = Prompt.ask(f"Enter new value ({min_val}-{max_val})", default=str(current))
            val = int(val_str)
            
            if min_val <= val <= max_val:
                return val
            else:
                console.print(f"[red]Value must be between {min_val} and {max_val}[/red]")
        except ValueError:
            console.print("[red]Invalid number[/red]")
        except KeyboardInterrupt:
            return current

def show_settings_menu():
    """Show settings menu with arrow key navigation."""
    cfg = config_manager.get_config_manager()
    
    while True:
        console.clear()
        
        # show current settings
        table = Table(title="[bold cyan]Current Settings[/bold cyan]", box=box.ROUNDED)
        table.add_column("Setting", style="cyan")
        table.add_column("Value", style="yellow")
        table.add_column("Description", style="dim")
        
        table.add_row("Typo Probability", f"{cfg.get('typo_probability') * 100:.1f}%", "Chance of making a typo per character")
        table.add_row("Edit Probability", f"{cfg.get('edit_probability') * 100:.1f}%", "Chance to go back and edit")
        table.add_row("Rephrase Probability", f"{cfg.get('sentence_rephrase_probability') * 100:.1f}%", "Chance to rephrase sentences")
        table.add_row("Base Delay Min", f"{cfg.get('base_delay_min')}ms", "Minimum delay between keystrokes")
        table.add_row("Base Delay Max", f"{cfg.get('base_delay_max')}ms", "Maximum delay between keystrokes")
        table.add_row("Thinking Pause Min", f"{cfg.get('thinking_pause_min')}ms", "Minimum thinking pause")
        table.add_row("Thinking Pause Max", f"{cfg.get('thinking_pause_max')}ms", "Maximum thinking pause")
        table.add_row("Sentence Pause Min", f"{cfg.get('sentence_pause_min')}ms", "Minimum pause at sentence end")
        table.add_row("Sentence Pause Max", f"{cfg.get('sentence_pause_max')}ms", "Maximum pause at sentence end")
        table.add_row("Comma Pause Min", f"{cfg.get('comma_pause_min')}ms", "Minimum pause at comma")
        table.add_row("Comma Pause Max", f"{cfg.get('comma_pause_max')}ms", "Maximum pause at comma")
        table.add_row("Use AI", "Yes" if cfg.get('use_ai') else "No", "Enable Gemini API features")
        table.add_row("Countdown Seconds", f"{cfg.get('countdown_seconds')}s", "Countdown before typing starts")
        table.add_row("Speed Multiplier", f"{cfg.get('speed_multiplier')}x", "Typing speed multiplier")
        
        console.print(table)
        console.print()
        
        # edit menu with arrow keys
        console.print("[bold cyan]Edit Settings[/bold cyan]\n")
        questions = [
            inquirer.List(
                'choice',
                message="Select setting to edit",
                choices=[
                    ('Typo Probability', '1'),
                    ('Edit Probability', '2'),
                    ('Rephrase Probability', '3'),
                    ('Base Delay (Min/Max)', '4'),
                    ('Thinking Pause (Min/Max)', '5'),
                    ('Sentence Pause (Min/Max)', '6'),
                    ('Comma Pause (Min/Max)', '7'),
                    ('Toggle AI', '8'),
                    ('Countdown Seconds', '9'),
                    ('Speed Multiplier', '10'),
                    ('Back to Main Menu', 'b'),
                ],
                carousel=True
            )
        ]
        
        answers = inquirer.prompt(questions)
        if not answers:
            cfg.save()
            break
        
        choice = answers['choice']
        
        if choice == "b":
            cfg.save()
            break
        elif choice == "1":
            val = edit_number_setting("Typo Probability", cfg.get('typo_probability'), 
                                     min_val=0.0, max_val=0.5, is_percent=True)
            cfg.set('typo_probability', val)
        elif choice == "2":
            val = edit_number_setting("Edit Probability", cfg.get('edit_probability'),
                                     min_val=0.0, max_val=1.0, is_percent=True)
            cfg.set('edit_probability', val)
        elif choice == "3":
            val = edit_number_setting("Rephrase Probability", cfg.get('sentence_rephrase_probability'),
                                     min_val=0.0, max_val=1.0, is_percent=True)
            cfg.set('sentence_rephrase_probability', val)
        elif choice == "4":
            min_val = edit_int_setting("Base Delay Min", cfg.get('base_delay_min'), min_val=10, max_val=500)
            max_val = edit_int_setting("Base Delay Max", cfg.get('base_delay_max'), min_val=min_val, max_val=1000)
            cfg.set('base_delay_min', min_val)
            cfg.set('base_delay_max', max_val)
        elif choice == "5":
            min_val = edit_int_setting("Thinking Pause Min", cfg.get('thinking_pause_min'), min_val=100, max_val=5000)
            max_val = edit_int_setting("Thinking Pause Max", cfg.get('thinking_pause_max'), min_val=min_val, max_val=10000)
            cfg.set('thinking_pause_min', min_val)
            cfg.set('thinking_pause_max', max_val)
        elif choice == "6":
            min_val = edit_int_setting("Sentence Pause Min", cfg.get('sentence_pause_min'), min_val=100, max_val=5000)
            max_val = edit_int_setting("Sentence Pause Max", cfg.get('sentence_pause_max'), min_val=min_val, max_val=10000)
            cfg.set('sentence_pause_min', min_val)
            cfg.set('sentence_pause_max', max_val)
        elif choice == "7":
            min_val = edit_int_setting("Comma Pause Min", cfg.get('comma_pause_min'), min_val=50, max_val=2000)
            max_val = edit_int_setting("Comma Pause Max", cfg.get('comma_pause_max'), min_val=min_val, max_val=5000)
            cfg.set('comma_pause_min', min_val)
            cfg.set('comma_pause_max', max_val)
        elif choice == "8":
            current = cfg.get('use_ai')
            new_val = not current
            cfg.set('use_ai', new_val)
            console.print(f"\n[green]AI {'enabled' if new_val else 'disabled'}[/green]")
            input("\nPress Enter to continue...")
        elif choice == "9":
            val = edit_int_setting("Countdown Seconds", cfg.get('countdown_seconds'), min_val=0, max_val=10)
            cfg.set('countdown_seconds', val)
        elif choice == "10":
            val = edit_number_setting("Speed Multiplier", cfg.get('speed_multiplier'),
                                     min_val=0.1, max_val=5.0, step=0.1)
            cfg.set('speed_multiplier', val)
        
        cfg.save()

def get_file_path() -> str | None:
    """Prompt user for file path."""
    console.clear()
    console.print("\n[cyan]Enter path to text file:[/cyan]\n")
    path = Prompt.ask("File path", default="")
    
    if not path:
        return None
    
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        console.print(f"[red]File not found: {path}[/red]")
        input("\nPress Enter to continue...")
        return None
    except Exception as e:
        console.print(f"[red]Error reading file: {e}[/red]")
        input("\nPress Enter to continue...")
        return None

def show_presets_menu():
    """Show presets menu and allow selection."""
    cfg = config_manager.get_config_manager()
    presets = cfg.get_presets()
    
    console.clear()
    console.print("[bold cyan]Presets[/bold cyan]\n")
    
    # show preset info
    table = Table(title="Available Presets", box=box.ROUNDED)
    table.add_column("Preset", style="cyan")
    table.add_column("Description", style="yellow")
    
    for key, preset in presets.items():
        table.add_row(preset['name'], preset['description'])
    
    console.print(table)
    console.print()
    
    # select preset
    questions = [
        inquirer.List(
            'preset',
            message="Select a preset to apply",
            choices=[
                (presets[key]['name'], key) for key in presets.keys()
            ] + [('Cancel', 'cancel')],
            carousel=True
        )
    ]
    
    answers = inquirer.prompt(questions)
    if answers and answers['preset'] != 'cancel':
        preset_key = answers['preset']
        if cfg.apply_preset(preset_key):
            console.print(f"\n[green]Applied preset: {presets[preset_key]['name']}[/green]")
        else:
            console.print(f"\n[red]Failed to apply preset[/red]")
        input("\nPress Enter to continue...")

def export_config_menu():
    """Export configuration to a file."""
    cfg = config_manager.get_config_manager()
    
    console.clear()
    console.print("[bold cyan]Export Configuration[/bold cyan]\n")
    
    default_path = str(config_manager.CONFIG_DIR / "typesim_export.yaml")
    path = Prompt.ask("Enter file path to export to", default=default_path)
    
    if cfg.export_config(path):
        console.print(f"\n[green]Configuration exported to: {path}[/green]")
    else:
        console.print(f"\n[red]Failed to export configuration[/red]")
    
    input("\nPress Enter to continue...")

def import_config_menu():
    """Import configuration from a file."""
    cfg = config_manager.get_config_manager()
    
    console.clear()
    console.print("[bold cyan]Import Configuration[/bold cyan]\n")
    
    path = Prompt.ask("Enter file path to import from", default="")
    
    if not path:
        console.print("[yellow]No path provided[/yellow]")
        input("\nPress Enter to continue...")
        return
    
    if Confirm.ask("[yellow]This will overwrite your current settings. Continue?[/yellow]"):
        if cfg.import_config(path):
            console.print(f"\n[green]Configuration imported from: {path}[/green]")
        else:
            console.print(f"\n[red]Failed to import configuration[/red]")
    else:
        console.print("[yellow]Import cancelled[/yellow]")
    
    input("\nPress Enter to continue...")
