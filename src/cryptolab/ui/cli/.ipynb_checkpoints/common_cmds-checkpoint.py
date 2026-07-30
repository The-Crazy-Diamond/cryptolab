import typer
from typing import List
from cryptolab.ciphers import CIPHERS
from cryptolab.analysis.methods import ANALYSIS_METHODS
from cryptolab.utils.io import load_input

def run_cipher(module, method_name, text, args):
    func = getattr(module, method_name)

    try:
        if args is None:
            result = func(text)
        else:
            result = func(text, *args)
    except TypeError as e:
        print(f"Invalid arguments for {module.NAME}: {e}")
        raise typer.Exit(1)

    print(result)

def create_command(method_name: str):
    def factory(module):
        args_help = getattr(module, "ARGS_HELP", None)

        # WITHOUT args
        if args_help is None:

            def command(
                input_data: str = typer.Argument(
                    ...,
                    help="Text or path to input file"
                )
            ):
                text = load_input(input_data)
                run_cipher(module, method_name, text, None)

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
                run_cipher(module, method_name, text, args)

        # Metadata (shared)
        command.__name__ = module.NAME

        description = getattr(module, "DESCRIPTION", "")
        command.__doc__ = f"""
        {description}
        
        Examples:
            cryptolab {method_name} {module.NAME} "HELLO" {module.ARGS_EXAMPLE}
            cryptolab {method_name} {module.NAME} file.txt {module.ARGS_EXAMPLE}
        """

        return command

    return factory


# List methods
#Removed because --help already reveals the list of methods as the list of commands (in a nicer way in fact)
# def list_methods(registry: dict, title: str):
#     print(f"{title}\n")

#     for name, module in sorted(registry.items()):
#         desc = getattr(module, "DESCRIPTION", "").strip()
#         print(f"- {name:<15} {desc}")

# def list_ciphers():
#     """List available ciphers"""
#     list_methods(CIPHERS, "Available ciphers:")


# def list_analysis_methods():
#     """List available analysis methods"""
#     list_methods(ANALYSIS_METHODS, "Available analysis methods:")
    
