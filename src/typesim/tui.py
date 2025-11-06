"""
Text User Interface for settings and configuration.
Uses inquirer for arrow-key navigation.
"""

import inquirer
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.table import Table
from rich.text import Text
from rich.align import Align
from rich import box
from typing import Callable, Any
from . import config_manager

console = Console()

# Credits footer to display on all menus
CREDITS = "made by pcstyle"

def print_header(title: str):
    """Print a minimal modern header with title."""
    console.print()
    console.print(f"  [bold cyan]{title}[/bold cyan]")
    console.print(f"  [dim]{'─' * len(title)}[/dim]")
    console.print()

def print_credits():
    """Print credits footer."""
    console.print()
    console.print(f"  [dim]{CREDITS}[/dim]")

def show_main_menu() -> str:
    """Show main menu with arrow key navigation."""
    console.clear()
    print_header("typesim")

    questions = [
        inquirer.List(
            'choice',
            message="",
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

    print_credits()
    console.print()
    answers = inquirer.prompt(questions)
    return answers['choice'] if answers else 'q'

def edit_number_setting(name: str, current: float, min_val: float = 0.0, max_val: float = 1.0,
                        step: float = 0.01, is_percent: bool = False) -> float:
    """Edit a number setting."""
    console.clear()
    print_header(name.lower())

    # Show current value
    current_display = current * 100 if is_percent else current
    suffix = "%" if is_percent else ""
    console.print(f"  [dim]current:[/dim] [yellow]{current_display:.2f}{suffix}[/yellow]")
    console.print()

    while True:
        try:
            if is_percent:
                range_hint = f"[dim]{min_val*100:.1f}-{max_val*100:.1f}%[/dim]"
                val_str = Prompt.ask(f"  {range_hint}", default=str(current * 100))
                val = float(val_str) / 100.0
            else:
                range_hint = f"[dim]{min_val}-{max_val}[/dim]"
                val_str = Prompt.ask(f"  {range_hint}", default=str(current))
                val = float(val_str)

            if min_val <= val <= max_val:
                print_credits()
                return val
            else:
                console.print(f"  [red]must be between {min_val} and {max_val}[/red]")
        except ValueError:
            console.print("  [red]invalid number[/red]")
        except KeyboardInterrupt:
            print_credits()
            return current

def edit_int_setting(name: str, current: int, min_val: int = 0, max_val: int = 10000) -> int:
    """Edit an integer setting."""
    console.clear()
    print_header(name.lower())

    # Show current value
    console.print(f"  [dim]current:[/dim] [yellow]{current}[/yellow]")
    console.print()

    while True:
        try:
            range_hint = f"[dim]{min_val}-{max_val}[/dim]"
            val_str = Prompt.ask(f"  {range_hint}", default=str(current))
            val = int(val_str)

            if min_val <= val <= max_val:
                print_credits()
                return val
            else:
                console.print(f"  [red]must be between {min_val} and {max_val}[/red]")
        except ValueError:
            console.print("  [red]invalid number[/red]")
        except KeyboardInterrupt:
            print_credits()
            return current

def show_settings_menu():
    """Show settings menu with arrow key navigation."""
    cfg = config_manager.get_config_manager()

    while True:
        console.clear()
        print_header("settings")

        # show current settings in minimal table
        table = Table(
            box=box.SIMPLE,
            show_header=False,
            show_edge=False,
            padding=(0, 2)
        )
        table.add_column(style="dim", no_wrap=True)
        table.add_column(style="yellow", justify="right")

        table.add_row("typo probability", f"{cfg.get('typo_probability') * 100:.1f}%")
        table.add_row("edit probability", f"{cfg.get('edit_probability') * 100:.1f}%")
        table.add_row("rephrase probability", f"{cfg.get('sentence_rephrase_probability') * 100:.1f}%")
        table.add_row("", "")
        table.add_row("base delay", f"{cfg.get('base_delay_min')}-{cfg.get('base_delay_max')}ms")
        table.add_row("thinking pause", f"{cfg.get('thinking_pause_min')}-{cfg.get('thinking_pause_max')}ms")
        table.add_row("sentence pause", f"{cfg.get('sentence_pause_min')}-{cfg.get('sentence_pause_max')}ms")
        table.add_row("comma pause", f"{cfg.get('comma_pause_min')}-{cfg.get('comma_pause_max')}ms")
        table.add_row("", "")
        table.add_row("use ai", "yes" if cfg.get('use_ai') else "no")
        table.add_row("countdown", f"{cfg.get('countdown_seconds')}s")
        table.add_row("speed", f"{cfg.get('speed_multiplier')}x")

        console.print(table)
        console.print()

        # edit menu with arrow keys
        questions = [
            inquirer.List(
                'choice',
                message="",
                choices=[
                    ('Typo Probability', '1'),
                    ('Edit Probability', '2'),
                    ('Rephrase Probability', '3'),
                    ('Base Delay', '4'),
                    ('Thinking Pause', '5'),
                    ('Sentence Pause', '6'),
                    ('Comma Pause', '7'),
                    ('Toggle AI', '8'),
                    ('Countdown', '9'),
                    ('Speed', '10'),
                    ('Back', 'b'),
                ],
                carousel=True
            )
        ]

        print_credits()
        console.print()
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

            console.clear()
            print_header("toggle ai")
            console.print(f"  [green]ai {'enabled' if new_val else 'disabled'}[/green]")
            print_credits()
            input("\n  [dim]press enter...[/dim]")
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
    print_header("load file")

    path = Prompt.ask("  [dim]path[/dim]", default="")

    if not path:
        print_credits()
        return None

    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            console.print()
            console.print("  [green]loaded[/green]")
            print_credits()
            input("\n  [dim]press enter...[/dim]")
            return content
    except FileNotFoundError:
        console.print()
        console.print(f"  [red]not found:[/red] [dim]{path}[/dim]")
        print_credits()
        input("\n  [dim]press enter...[/dim]")
        return None
    except Exception as e:
        console.print()
        console.print(f"  [red]error:[/red] [dim]{e}[/dim]")
        print_credits()
        input("\n  [dim]press enter...[/dim]")
        return None

def show_presets_menu():
    """Show presets menu and allow selection."""
    cfg = config_manager.get_config_manager()
    presets = cfg.get_presets()

    console.clear()
    print_header("presets")

    # show preset info
    table = Table(
        box=box.SIMPLE,
        show_header=False,
        show_edge=False,
        padding=(0, 2)
    )
    table.add_column(style="cyan", no_wrap=True)
    table.add_column(style="dim")

    for key, preset in presets.items():
        table.add_row(preset['name'], preset['description'])

    console.print(table)
    console.print()

    # select preset
    questions = [
        inquirer.List(
            'preset',
            message="",
            choices=[
                (presets[key]['name'], key) for key in presets.keys()
            ] + [('Cancel', 'cancel')],
            carousel=True
        )
    ]

    print_credits()
    console.print()
    answers = inquirer.prompt(questions)
    if answers and answers['preset'] != 'cancel':
        preset_key = answers['preset']
        if cfg.apply_preset(preset_key):
            console.print()
            console.print(f"  [green]applied {presets[preset_key]['name']}[/green]")
        else:
            console.print()
            console.print("  [red]failed[/red]")

        print_credits()
        input("\n  [dim]press enter...[/dim]")

def export_config_menu():
    """Export configuration to a file."""
    cfg = config_manager.get_config_manager()

    console.clear()
    print_header("export config")

    default_path = str(config_manager.CONFIG_DIR / "typesim_export.yaml")
    path = Prompt.ask("  [dim]path[/dim]", default=default_path)

    if cfg.export_config(path):
        console.print()
        console.print(f"  [green]exported to {path}[/green]")
    else:
        console.print()
        console.print("  [red]failed[/red]")

    print_credits()
    input("\n  [dim]press enter...[/dim]")

def import_config_menu():
    """Import configuration from a file."""
    cfg = config_manager.get_config_manager()

    console.clear()
    print_header("import config")

    path = Prompt.ask("  [dim]path[/dim]", default="")

    if not path:
        console.print("  [yellow]no path[/yellow]")
        print_credits()
        input("\n  [dim]press enter...[/dim]")
        return

    if Confirm.ask("  [yellow]overwrite current settings?[/yellow]"):
        if cfg.import_config(path):
            console.print()
            console.print(f"  [green]imported from {path}[/green]")
        else:
            console.print()
            console.print("  [red]failed[/red]")
    else:
        console.print()
        console.print("  [yellow]cancelled[/yellow]")

    print_credits()
    input("\n  [dim]press enter...[/dim]")
