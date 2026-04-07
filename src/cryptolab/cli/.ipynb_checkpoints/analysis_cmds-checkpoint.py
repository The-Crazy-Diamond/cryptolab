import typer
from pathlib import Path
from cryptolab.utils.io import load_input
# from cryptolab.analysis.monoalphabetic_decoder import (
#     MonoalphabeticSubstitutionDecoder,
# )

app = typer.Typer()


# @app.command("monoalphabetic")
# def monoalphabetic_solver(input_data: str):
#     """Interactive monoalphabetic substitution solver."""
    
#     ciphertext = load_input(input_data)
    
#     decoder = MonoalphabeticSubstitutionDecoder(ciphertext)

#     print("\n=== Monoalphabetic Decoder ===\n")

#     while True:
#         print("CIPHERTEXT:")
#         print(decoder.ciphertext)
#         print("\nPLAINTEXT:")
#         print(decoder.get_plaintext())
#         print()

#         command = input("Enter command (e.g. Xe, 'quit'): ").strip()

#         if command.lower() in {"quit", "exit"}:
#             break

#         if len(command) == 2:
#             c, p = command[0], command[1]
#             decoder.apply_mapping(c, p)
#         else:
#             print("Invalid command. Use format like Xe")

@app.command()
def frequency(input_data: str):
    text = load_input(input_data)
    print(compute_frequency(text))