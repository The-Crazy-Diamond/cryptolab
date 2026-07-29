import shutil
import textwrap

# Output helpers for CLI:

# pretty tables
# aligned frequency output
# color helpers (if using rich)

def clear_screen() -> None:
    # ANSI escape sequence to clear the screen
    print("\033[H\033[J", end="")

    
def print_stacked(*strings, width=None, break_long_words=True):
    """
    Print multiple texts stacked line-by-line.

    Args:
        *strings: any number of input strings
        width: max line width (defaults to terminal width)
        break_long_words: whether to break long words (useful for ciphertext)
    """
    if width is None:
        width = shutil.get_terminal_size(fallback=(120, 20)).columns

    wrapped_blocks = [
        textwrap.wrap(
            s,
            width=width,
            break_long_words=break_long_words,
            break_on_hyphens=break_long_words,
        )
        for s in strings
    ]

    max_lines = max(len(block) for block in wrapped_blocks)

    # Pad all blocks to same height
    for block in wrapped_blocks:
        block += [""] * (max_lines - len(block))

    # Print stacked
    for i in range(max_lines):
        for block in wrapped_blocks:
            print(block[i])
        print()  # blank line between groups

def print_banner(*titles, width=None, symbol='='):
    """
    Print one or more centered title lines surrounded by a repeated symbol.

    Parameters
    ----------
    *titles:
        Titles to display. An empty string prints a separator line.
    width:
        Total width of each line. Defaults to the terminal width.
    symbol:
        Character used to fill the line.
    """
    if width is None:
        width = shutil.get_terminal_size(fallback=(120, 20)).columns

    for title in titles:
        title = f" {title} " if title else ""

        padding = width - len(title)
        left = max(0, padding // 2)
        right = max(0, padding - left)

        print(symbol * left + title + symbol * right)
    