import typer
from cryptolab.cli import cipher_cmds, decipher_cmds, analysis_cmds


app = typer.Typer(
    help="Cryptolab: A CLI tool to experiment with classical ciphers and cryptanalysis."
)

# Attach subcommands
app.add_typer(cipher_cmds.app, name="encrypt", help="Encrypt text using ciphers")
app.add_typer(decipher_cmds.app, name="decrypt", help="Decrypt text using ciphers")
app.add_typer(analysis_cmds.app, name="analyse", help="Cryptanalysis tools")

# before encrypt, decrypt and analyse were cipher, decipher and analysis

if __name__ == "__main__":
    app()