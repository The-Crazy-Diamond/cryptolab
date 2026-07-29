import shlex
from cryptolab.utils.formatting import clear_screen, print_banner

class Shell:
    TITLE = ""
    PROMPT = "shell> "
    def __init__(self):
        self.running = True
        self.status = None
        self.commands = self.build_commands()

    def build_commands(self):
        return {
            "help": self.do_help,
            "quit": self.do_quit,
            "q": self.do_quit,
            "exit": self.do_quit,
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
        func = self.commands.get(cmd)
        
        if func is None:
            self.status = f"Unknown command: {cmd}."
            self.display()
            return

        # Executing
        try:
            func(*args)
        except TypeError:
            self.status = f"Invalid arguments for '{cmd}'."
        except ValueError as e:
            self.status = str(e)
        except NotImplementedError as e:
            self.status = str(e)

        # Refresh the display
        self.display()

    def do_help(self):
        raise NotImplementedError("Helper not implemented")    
     
    def do_quit(self):
        self.status = "Goodbye!"
        self.running = False