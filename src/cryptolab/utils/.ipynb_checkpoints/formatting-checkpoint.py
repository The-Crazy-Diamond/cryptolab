import shutil
import textwrap

# Output helpers for CLI:

# pretty tables
# aligned frequency output
# color helpers (if using rich)

def clear_screen() -> None:
    # ANSI escape sequence to clear the screen
    print("\033[H\033[J", end="")

    
def print_stacked(*strings, width=None, break_long_words=False):
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