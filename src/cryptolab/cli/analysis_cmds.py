import typer
from cryptolab.analysis import ANALYSIS_TOOLS
from cryptolab.cli.common_cmds import create_command, list_analysis_tools

app = typer.Typer()

factory = create_command("analyse")

for name, module in ANALYSIS_TOOLS.items():
    app.command(name)(factory(module))

app.command("list")(list_analysis_tools)
