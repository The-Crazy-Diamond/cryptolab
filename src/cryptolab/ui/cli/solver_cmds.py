import typer

from cryptolab.utils.io import load_input
from cryptolab.analysis.solvers import monoalphabetic

app = typer.Typer()

@app.command(monoalphabetic.NAME)
def mono(input_data: str):
    monoalphabetic.solve(load_input(input_data))