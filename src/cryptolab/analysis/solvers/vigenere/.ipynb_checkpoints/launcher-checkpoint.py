from cryptolab.analysis.solvers.vigenere.session import VigenereSession
from cryptolab.ui.repl.vigenere_shell import VigenereShell

def solve(ciphertext: str):
    session = VigenereSession(ciphertext)
    VigenereShell(session).run()
