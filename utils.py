
from rich.console import Console

def write(console: Console, marker, color, text):
	console.print(f"[bold {color}]({marker})[/] [{color}]{text}[/]")
