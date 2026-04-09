import typer
from typing import List
from cryptolab.ciphers import CIPHERS
from cryptolab.utils.io import load_input


def create_command(method_name: str):
    """
    method_name: "encrypt" or "decrypt"
    """
    def factory(cipher_module):
        def command(
            input_data: str,
            args: List[str] = typer.Argument([])
        ):
            """Process text or file using this cipher."""
            text = load_input(input_data)

            func = getattr(cipher_module, method_name)

            try:
                result = func(text, *args)
            except TypeError as e:
                print(f"Invalid arguments: {e}")
                raise typer.Exit(1)

            print(result)

        command.__name__ = cipher_module.NAME
        command.__doc__ = getattr(
            cipher_module,
            "DESCRIPTION",
            f"{cipher_module.NAME} cipher",
        )

        return command

    return factory
    
def list_ciphers():
    """List available ciphers."""
    
    print("Available ciphers:")
    for name in sorted(CIPHERS.keys()):
        print(f"- {name}")