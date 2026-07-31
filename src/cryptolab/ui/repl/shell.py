import shlex
from cryptolab.utils.formatting import clear_screen, print_banner

class Shell:
    TITLE = ""
    PROMPT = "shell> "
    def __init__(self):
        self.running = True
        self.status = "Type 'help' to show commands."
        self.commands = self.build_commands()
        self.aliases = self.build_aliases()

    def build_commands(self):
        return {
            "help": self.do_help,
            "quit": self.do_quit,
            "exit": self.do_quit,
        }
        
    def build_aliases(self):
        return {
            "q": "quit",
        }
        
    def display(self):
        # 1.Generic preamble
        clear_screen()
        print_banner("CRYPTOLAB",self.TITLE)
        # 2. Tool-specific content
        self.display_content()
        # 3. Generic epilogue
        print_banner('')
        self.display_status()

    def display_content(self):
        pass

    def display_status(self):
        if self.status is not None:
            print()
            print(self.status)
    
    # REPL running methods
    def run(self):
        self.display()
    
        while self.running:
            command = input(self.PROMPT).strip()
            self.execute(command)
    
    def execute(self, command: str):
        self.status = None
        if not command:
            self.display()
            return
            
        # Parsing command
        parts = shlex.split(command)
        
        cmd = parts[0]
        args = parts[1:]

        # Getting the associated function
        ## Resolve alias
        cmd = self.aliases.get(cmd, cmd)
        
        func = self.commands.get(cmd)
        
        if func is None:
            self.status = f"Unknown command: {cmd}."
            self.display()
            return

        # Executing
        handled = False
        try:
            result = func(*args)
            handled = (result is True)
        except TypeError:
            self.status = f"Invalid arguments for '{cmd}'."
        except ValueError as e:
            self.status = str(e)
        except NotImplementedError as e:
            self.status = str(e)

        # Refresh the display
        if not handled:
            self.display()

    def do_help(self, command=None):
        """Show available commands or help for a specific command."""
    
        if command is None:
            print("Available commands:\n")
    
            for name in sorted(self.commands):
                func = self.commands[name]
    
                aliases = sorted(
                    alias
                    for alias, target in self.aliases.items()
                    if target == name
                )
    
                doc = (func.__doc__ or "").strip().splitlines()
                summary = doc[0] if doc else ""
    
                alias_text = f" ({', '.join(aliases)})" if aliases else ""
    
                print(f"  {name:<12}{alias_text} {summary}")
            return True
    
            print("\nType 'help <command>' for details.")
            return True
    
        # Resolve aliases
        command = self.aliases.get(command, command)
    
        func = self.commands.get(command)
    
        if func is None:
            raise ValueError(f"Unknown command '{command}'.")
    
        print(func.__doc__ or "No help available.")
        return True
        # True is returned when do_help() prints something itself
     
    def do_quit(self):
        """
        Quit session.

        Usage:
            quit
        """
        self.status = "Goodbye!"
        self.running = False