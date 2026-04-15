import typer
from typing import List
from cryptolab.ciphers import CIPHERS
from cryptolab.utils.io import load_input

def run_cipher(cipher_module, method_name, text, args):
    func = getattr(cipher_module, method_name)

    try:
        if args is None:
            result = func(text)
        else:
            result = func(text, *args)
    except TypeError as e:
        print(f"Invalid arguments for {cipher_module.NAME}: {e}")
        raise typer.Exit(1)

    print(result)

def create_command(method_name: str):
    def factory(cipher_module):
        args_help = getattr(cipher_module, "ARGS_HELP", None)

        # WITHOUT args
        if args_help is None:

            def command(
                input_data: str = typer.Argument(
                    ...,
                    help="Text or path to input file"
                )
            ):
                text = load_input(input_data)
                run_cipher(cipher_module, method_name, text, None)

        # WITH args
        else:

            def command(
                input_data: str = typer.Argument(
                    ...,
                    help="Text or path to input file"
                ),
                args: List[str] = typer.Argument(
                    None,
                    help=args_help
                )
            ):
                args = args or []
                text = load_input(input_data)
                run_cipher(cipher_module, method_name, text, args)

        # Metadata (shared)
        command.__name__ = cipher_module.NAME

        description = getattr(cipher_module, "DESCRIPTION", "")
        command.__doc__ = f"""
        {description}
        
        Examples:
            cryptolab cipher {cipher_module.NAME} "HELLO" {cipher_module.ARGS_EXAMPLE}
            cryptolab cipher {cipher_module.NAME} file.txt {cipher_module.ARGS_EXAMPLE}
        """

        return command

    return factory


def list_ciphers():
    """List available ciphers"""
    
    print("Available ciphers:\n")
    
    for name, module in sorted(CIPHERS.items()):
        desc = getattr(module, "DESCRIPTION", "")
        print(f"- {name:<15} {desc}")
