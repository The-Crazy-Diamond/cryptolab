import typer
from cryptolab.ciphers import CIPHERS
from cryptolab.cli.common_cmds import create_command, list_ciphers

app = typer.Typer()

factory = create_command("decrypt")

for name, module in CIPHERS.items():
    app.command(name)(factory(module))

app.command("list")(list_ciphers)