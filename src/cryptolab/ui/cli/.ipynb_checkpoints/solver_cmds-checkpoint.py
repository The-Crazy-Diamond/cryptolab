import typer

from cryptolab.utils.io import load_input
from cryptolab.analysis.solvers import caesar_bruteforce, affine_bruteforce
from cryptolab.analysis.solvers import monoalphabetic, polyalphabetic, vigenere

app = typer.Typer()

# CLI solvers (single file)
@app.command(caesar_bruteforce.NAME)
def caesar(input_data: str):
    text = load_input(input_data)
    caesar_bruteforce.solve(text)

@app.command(affine_bruteforce.NAME)
def affine(input_data: str, argument:str):
    text = load_input(input_data)
    affine_bruteforce.solve(text, argument)


# REPL solvers (folder)
@app.command(monoalphabetic.NAME)
def mono(input_data: str):
    text = load_input(input_data)
    monoalphabetic.solve(text)

@app.command(polyalphabetic.NAME)
def poly(input_data: str):
    text = load_input(input_data)
    polyalphabetic.solve(text)

@app.command(vigenere.NAME)
def vige(input_data: str):
    text = load_input(input_data)
    vigenere.solve(text)


