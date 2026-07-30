"""
Analysis tool plugin template for Cryptolab.

To add a new analysis tool:
1. Copy this file (with "cp _template.py your_tool.py")
2. Rename it (e.g. kasiski.py, frequency.py)
3. Update attributes
4. Implement analyse
"""

NAME = "your_tool_name"
DESCRIPTION = "brief description of what is this tool"
ARGS_HELP = "list of required arguments: name (type) (write None if no argument is required)"
ARGS_EXAMPLE = "example (write \"\" if no argument is required)"


def analyse(text: str, *args: str):
    raise NotImplementedError("Method function not implemented")
