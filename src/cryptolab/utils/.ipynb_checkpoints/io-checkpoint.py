from pathlib import Path

def load_input(input_data: str) -> str:
    """Load text from a file or return raw input."""
    
    path = Path(input_data)
    if path.exists() and path.is_file():
        return path.read_text()
    
    return input_data