
import math
from utils import write
from rich.console import Console
console = Console()

from transformers import pipeline

console.print("[italic blue](...) loading system[/]")
classifier = pipeline(model="facebook/bart-large-mnli")
console.print("[italic green](...) system loaded")

labels = [
	"love",
	"hate",
	"neutral"
]

def classify(text):
    
	model_output = classifier(text, candidate_labels=labels)

	max_score = -math.inf
	max_label = ""

	for score, label in zip(model_output["scores"], model_output["labels"]):

		if score > max_score:
			max_score = score
			max_label = label

	return (max_label, max_score)

def main():
	
	try:
		while True:
			
			prompt = console.input("[bold purple](?)[/] ")
			label, score = classify(prompt)
			write(console, "!", "yellow", str((label, score)))

	except KeyboardInterrupt:
		console.print(" ")
		write(console, "X", "red", "Goodbye!")

if __name__ == "__main__":
	main()
