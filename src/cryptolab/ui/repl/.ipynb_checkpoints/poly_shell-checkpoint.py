from cryptolab.ui.repl.shell import Shell
from cryptolab.analysis.solvers.polyalphabetic.session import PolySession
from cryptolab.utils.text import add_spaces
from cryptolab.utils.formatting import print_stacked
from cryptolab.analysis.methods.frequency import get_frequencies
from cryptolab.analysis.methods.kasiski import analyse as kasiski_test
from cryptolab.analysis.methods.coincidence_test import analyse as ioc_test
import json
from pathlib import Path

class PolyShell(Shell):

    TITLE = "Polyalphabetic substitution"
    PROMPT = "poly> "
    def __init__(self, session: PolySession):
        super().__init__()
        self.session = session
        self.visible_frequencies = set()
        self.frequencies_cache = {}
        self.status = "Polyalphabetic session initialized. \n" + self.status
        

    def build_commands(self):
        commands = super().build_commands()
        commands.update({
            "map": self.do_map,
            "unmap": self.do_unmap,
            "swap": self.do_swap,
            "reset": self.do_reset,
            
            "frequencies": self.do_frequencies,
            "kasiski": self.do_kasiski,
            "ioc": self.do_ioc,

            "keylen": self.do_set_key_length,
            "active": self.do_set_active_index,
            "show": self.do_show,
            "undo": self.do_undo,
            "redo": self.do_redo,
    
            "save": self.do_save,
            "load": self.do_load,
        })

        return commands

    def build_aliases(self):
        aliases = super().build_aliases()
        aliases.update({
            "m": "map",
            "u": "unmap",
            "s": "swap",
            "r": "reset",
            
            "freq": "frequencies",

            "k": "keylen",
            "a": "active",
        })

        return aliases

    def display_content(self):
       
        if self.session.key_length is None:
            index_line = ""
        else:
            indicators = []
            letter_index = 0
        
            for c in self.session.ciphertext:
                if c.isalpha():
                    if letter_index % self.session.key_length == self.session.active_index:
                        indicators.append('^')
                    else:
                        indicators.append(' ')
                    letter_index += 1
                else:
                    indicators.append(' ')
        
            index_line = "".join(indicators)
            
        print_stacked(
            add_spaces(self.session.ciphertext),
            add_spaces(self.session.plaintext),
            add_spaces(index_line),    
        )

        if self.session.key_length is None:
            key_length = "undefined"
            active_index = "undefined"
        else:
            key_length = self.session.key_length
            active_index = self.session.active_index
        print(f"Key length = {key_length} ; Active index = {active_index}")
        
        if self.visible_frequencies:
            print(f"Key index | Frequencies for indices mod {self.session.key_length} \n")
            for n in sorted(self.visible_frequencies):
                print(f"{n:9} : {self.frequencies_cache[n]}\n")

    # Modifying commands
    # def treat_index(self, key_index):
    #     self.session.key_length_check()
    #     if key_index == None:
    #         key_index = self.session.active_index
    #     if key_index in ['a','all']:
    #         return key_index
    #     return int(key_index) % self.session.key_length
    def treat_index(self, key_index):
        self.session.key_length_check()
    
        if key_index is None:
            return self.session.active_index
    
        if isinstance(key_index, str) and key_index.lower() in ("a", "all"):
            return "all"
    
        return int(key_index) % self.session.key_length
        
    def do_map(self, cipher, plain, key_index = None):
        """
        Assign a plaintext letter to a ciphertext letter at every index that are congruent to a key index modulo the key's length.
    
        Usage:
            map <cipher> <plain> <key_index>
    
        Example:
            map X e 2
        """
        key_index = self.treat_index(key_index)
        self.session.assign(cipher, plain, key_index)
        self.status = f"Mapped {cipher} -> {plain} at indices {key_index} mod {self.session.key_length}"

    def do_unmap(self, cipher, key_index = None):
        """
        Unassign the plaintext letter of a ciphertext letter at every index that are congruent to a key index modulo the key's length.
    
        Usage:
            unmap <cipher> <key_index>
    
        Example:
            unmap X 3
        """
        key_index = self.treat_index(key_index)
        self.session.unassign(cipher, key_index)
        self.status = f"Unassigned {cipher} at indices {key_index} mod {self.session.key_length}"

    def do_swap(self, cipher1, cipher2, key_index = None):
        """
        Swap two existing assignments at every index that are congruent to a key index modulo the key's length.
    
        Usage:
            swap <cipher1> <cipher2> <key_index>
    
        Example:
            swap X Y 1
        """
        key_index = self.treat_index(key_index)
        self.session.swap(cipher1, cipher2, key_index)
        self.status = f"Swapped {cipher1} <-> {cipher2} at indices {key_index} mod {self.session.key_length}"
    
    def do_reset(self):
        """
        Reset the session.
    
        Usage:
            reset
        """
        self.session.reset()
        self.visible_frequencies = set()
        self.frequencies_cache = {}
        self.status = "Session reset."

    # Analysis commands          
    # def do_frequencies(self, key_index = None):
    #     """
    #     Toggle the display of letter frequencies at every index that are congruent to a key index modulo the key's length.
        
    #     Usage:
    #          frequencies <key_index>
    
    #     Example:
    #          frequencies 4
    #     """
    #     key_index = self.treat_index(key_index)
        
    #     if key_index in ["all","a"]:
    #         if len(self.visible_frequencies) == self.session.key_length:
    #             self.visible_frequencies = set()
    #         else:
    #             self.visible_frequencies = set(range(self.session.key_length))
    #             for key_index in range(self.session.key_length):
    #                 self.frequencies_cache[key_index] = get_frequencies(self.session.get_mono_session(key_index).ciphertext)
    #             self.status = f"Cached frequencies for all indices."
    #     else:
    #         if key_index in self.visible_frequencies:
    #             self.visible_frequencies.remove(key_index)
    #         else:
    #             self.visible_frequencies.add(key_index)
    #         self.status = None
    
    #         if key_index not in self.frequencies_cache:
    #             self.frequencies_cache[key_index] = get_frequencies(self.session.get_mono_session(key_index).ciphertext)
    #             self.status = f"Cached frequencies for indices congruent to {key_index} mod {self.session.key_length}"

    def _cache_frequencies(self, key_index):
        """Ensure frequencies for one key index are cached."""
        if key_index not in self.frequencies_cache:
            self.frequencies_cache[key_index] = get_frequencies(
                self.session.get_mono_session(key_index).ciphertext
            )
            return True
        return False


    def do_frequencies(self, key_index=None):
        """
        Toggle the display of letter frequencies.
    
        Usage:
            frequencies [index|all]
        """
        key_index = self.treat_index(key_index)
    
        # Toggle all
        if key_index in ("all", "a"):
            if len(self.visible_frequencies) == self.session.key_length:
                self.visible_frequencies.clear()
                self.status = None
            else:
                self.visible_frequencies = set(range(self.session.key_length))
    
                newly_cached = 0
                for i in range(self.session.key_length):
                    if self._cache_frequencies(i):
                        newly_cached += 1
    
                self.status = (
                    f"Cached frequencies for {newly_cached} new indices."
                    if newly_cached
                    else None
                )
            return
    
        # Toggle one index
        if key_index in self.visible_frequencies:
            self.visible_frequencies.remove(key_index)
        else:
            self.visible_frequencies.add(key_index)
    
        if self._cache_frequencies(key_index):
            self.status = (
                f"Cached frequencies for index {key_index}."
            )
        else:
            self.status = None
    
    def do_kasiski(self, ngram_size = 3, key_length_bound = 10, score_margin = 5):
        """
        Perform Kasiski's test to estimate the key's length.
        
        Usage:
             kasiski <ngram_size> <key_length_bound> <score_margin>
    
        Example:
             kasiski 4 9 3
        """
        kasiski_test(self.session.ciphertext, ngram_size, key_length_bound, score_margin)
        return True # Returning True allows test to display the resutls
        
    def do_ioc(self, key_length_bound = 10, coincidence_threshold = 0.06):
        """
        Perform tests using the index of coincidence to estimate the key's length.
        
        Usage:
             ioc <key_length_bound> <coincidence_threshold>
    
        Example:
             ioc 9 0.062
        """
        ioc_test(self.session.ciphertext, key_length_bound, coincidence_threshold)
        return True # Returning True allows test to display the resutls
        
        

    # Session commands
    def do_set_key_length(self, key_length):
        """
        Set the key's length.
        
        Usage:
             setKey <key_length>
    
        Example:
             setKey 6
        """
        key_length = int(key_length)
        self.session.set_key_length(key_length)
        self.visible_frequencies = set()
        self.frequencies_cache = {}
        self.status = f"Key length set to {key_length}."

    def do_set_active_index(self, key_index):
        """
        Set the active key index.
        
        Usage:
             setActive <key_index>
    
        Example:
             setActive 2
        """
        key_index = int(key_index)
        self.session.set_active_index(key_index)
        self.status = f"Active key index set to {key_index}."
    
    def do_show(self):
        """
        Print the current plaintext state.
    
        Usage:
            show
        """
        self.status = f"Plaintext: '{self.session.plaintext}'"

    def do_undo(self):
        """
        Undo last command.
    
        Usage:
            undo
        """
        self.session.undo()
        self.status = "Undo."
    
    def do_redo(self):
        """
        Redo previous undone command.
    
        Usage:
            redo
        """
        self.session.redo()
        self.status = "Redo."

    # Saving/loading commands
        
    def do_save(self, filename="polyalphabetic.json"):
        """
        Save the session in a JSON file. (By thefault, filename is "polyalphabetic.json".)
    
        Usage:
            save <filename>
    
        Example:
            save my_session.json
        """
        raise NotImplementedError
        # path = Path(filename)
    
        # if path.exists():
        #     answer = input(f"'{filename}' already exists. Overwrite? [y/N] ")
        #     if answer.lower() not in ("y", "yes"):
        #         self.status = "Save cancelled."
        #         return
    
        # with path.open("w") as f:
        #     json.dump(self.session.to_dict(), f, indent=4)
    
        # self.status = f"Session saved to '{filename}'."
        
    def do_load(self, filename="polyalphabetic.json"):
        """
        Load the session from a JSON file.
    
        Usage:
            load <filename>
    
        Example:
            load polyalphabetic.json
        """
        raise NotImplementedError
        # path = Path(filename)
    
        # if not path.exists():
        #     raise ValueError(f"'{filename}' does not exist.")
    
        # with path.open() as f:
        #     data = json.load(f)

        # if data["analyse_tool"] != "polyalphabetic":
        #     raise ValueError("Not a polyalphabetic session.")
    
        # session = MonoSession(data["ciphertext"])
        # session._mapping = data["mapping"]
    
        # self.session = session
        # self.status = f"Session loaded from '{filename}'."
        
        
    
"""
Commands to add:

[] suggest
[] score
[] dictionary
[] auto
"""
