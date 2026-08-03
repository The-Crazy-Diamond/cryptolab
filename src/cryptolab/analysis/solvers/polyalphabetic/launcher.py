from cryptolab.analysis.solvers.polyalphabetic.session import PolySession
from cryptolab.ui.repl.poly_shell import PolyShell

def solve(ciphertext: str):
    session = PolySession(ciphertext)
    PolyShell(session).run()