from typer import Argument
from needle.cmd.__app import app

__choices = ["inject", "append", "prepend"]

@app.command()
def write(mode: str = Argument(help="Mode to write in", default="inject")):

    print(f"Writing in mode: {mode}")
