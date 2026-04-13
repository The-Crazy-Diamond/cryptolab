import typer
from pathlib import Path
from cryptolab.utils.io import load_input


app = typer.Typer()


# @app.command()
# def frequency(input_data: str):
#     text = load_input(input_data)
#     print(compute_frequency(text))