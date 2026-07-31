from cryptolab.analysis.solvers.monoalphabetic.session import MonoSession
from cryptolab.ui.repl.mono_shell import MonoShell

def solve(text: str = ''):
    session = MonoSession(text)
    MonoShell(session).run()