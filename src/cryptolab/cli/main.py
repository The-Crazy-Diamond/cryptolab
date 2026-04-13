import typer
from cryptolab.cli import cipher_cmds, decipher_cmds
from cryptolab.cli import analysis_cmds


app = typer.Typer(
    help="Cryptolab: A CLI tool to experiment with classical ciphers and cryptanalysis."
)

# Attach subcommands
app.add_typer(cipher_cmds.app, name="cipher", help="Encrypt text using ciphers")
app.add_typer(decipher_cmds.app, name="decipher", help="Decrypt text using ciphers")
app.add_typer(analysis_cmds.app, name="analysis", help="Cryptanalysis tools")



if __name__ == "__main__":
    app()