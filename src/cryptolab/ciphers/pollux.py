NAME = "pollux"
DESCRIPTION = "brief description of what is this cipher"
ARGS_HELP = "list of required arguments: name (type)" 
ARGS_EXAMPLE = "example"


def encrypt(text: str, *args: str) -> str:
    raise NotImplementedError("Encrypt function not implemented")


def decrypt(text: str, *args: str) -> str:
    raise NotImplementedError("Decrypt function not implemented")
