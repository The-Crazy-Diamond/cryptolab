from cryptolab.analysis.solvers.monoalphabetic.session import MonoSession
from cryptolab.ui.repl.mono_shell import MonoShell

def solve(ciphertext: str):
    session = MonoSession(ciphertext)
    MonoShell(session).run()