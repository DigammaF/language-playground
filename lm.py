
from rich.console import Console
from utils import write
console = Console()

console.print("[italic blue](...) loading system[/]")
import languagemodels as lm
console.print("[italic green](...) system loaded[/]")

def ask(infos, question):
	return lm.chat(
		f"""
		System: Respond as a helpful assistant. {'. '.join(infos)}
		User: {question}
		Assistant:
		"""
	)

def main():
	
	write(console, "$", "blue", "setting up system")
	lm.set_max_ram(8)
	write(console, "^", "green", "system ready")

	infos = [
		"my name is Zoe",
		"I am 8",
		"I am cute",
		"the user's name is Hero",
		"the tavern is on the other side of town"
	]

	try:
		while True:
			prompt = console.input("[bold purple](?)[/] ")
			answer = ask(infos, prompt)
			write(console, "!", "yellow", answer)

	except KeyboardInterrupt:
		console.print(" ")
		write(console, "X", "red", "goodbye!")

if __name__ == "__main__":
	main()
