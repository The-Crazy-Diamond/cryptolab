import typer

from cryptolab.analysis.solvers import monoalphabetic

app = typer.Typer()

@app.command(monoalphabetic.NAME)
def mono(ciphertext: str):
    monoalphabetic.solve(ciphertext)