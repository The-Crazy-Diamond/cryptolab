# ###
# # These first lines should allow to enter via main.py 
# import sys
# from pathlib import Path

# sys.path.insert(0, str(Path.cwd().parents[2] / "src"))
# ###

import typer
from cryptolab.cli import cipher_cmds, decipher_cmds
from cryptolab.cli import analysis_cmds


app = typer.Typer()

# Attach subcommands
app.add_typer(cipher_cmds.app, name="cipher")
app.add_typer(decipher_cmds.app, name="decipher")

app.add_typer(analysis_cmds.app, name="analyze")


if __name__ == "__main__":
    app()