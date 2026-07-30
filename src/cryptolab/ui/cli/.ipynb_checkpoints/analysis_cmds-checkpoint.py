import typer
from cryptolab.analysis.methods import ANALYSIS_METHODS
from cryptolab.ui.cli.common_cmds import create_command#, list_analysis_methods

app = typer.Typer()

factory = create_command("analyse")

for name, module in ANALYSIS_METHODS.items():
    app.command(name)(factory(module))

# app.command("list")(list_analysis_methods)
