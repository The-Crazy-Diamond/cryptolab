from cryptolab.ciphers import CIPHERS
from pathlib import Path
from cryptolab.utils.io import load_input

def create_command(method_name: str):
    """
    method_name: "encrypt" or "decrypt"
    """

    def factory(cipher_module):
        def command(input_data: str, key: str):
            """Process text or file using this cipher."""

            text = load_input(input_data)

            # Dynamically call encrypt or decrypt
            func = getattr(cipher_module, method_name)
            result = func(text, key)

            print(result)

        # Important for Typer
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