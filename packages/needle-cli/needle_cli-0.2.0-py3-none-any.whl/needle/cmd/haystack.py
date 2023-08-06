from typer import Argument
from needle.cmd.__app import app



@app.command()
def find(mode: str = Argument(help="Mode to write in", default="inject")):

    print(f"Writing in mode: {mode}")
