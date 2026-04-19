from pathlib import Path


# Input/output utilities:

# read text from file / stdin
# write output safely
# maybe encoding handling

def load_input(input_data: str) -> str:
    """Load text from a file or return raw input."""
    
    path = Path(input_data)
    if path.exists() and path.is_file():
        return path.read_text()
    
    return input_data
    

def clear_screen() -> None:
    # ANSI escape sequence to clear the screen
    print("\033[H\033[J", end="")