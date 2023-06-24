
from utils import write
from rich.console import Console
console = Console()

from transformers import pipeline

console.print("[italic blue](...) loading system[/]")
model = pipeline(model="PygmalionAI/pygmalion-6b")
console.print("[italic green](...) system loaded")

def main():
    
    try:
        while True:
            prompt = console.input("[bold purple](?)[/] ")
            answer = model(prompt)
            write(console, "!", "yellow", answer)
        
    except KeyboardInterrupt:
        console.print(" ")
        write(console, "X", "red", "Goodbye!")

if __name__ == "__main__":
    pass
