from ..token import *

KEY_WORLD = {
    "IF"
    
}

class Parser:


    def __init__(self, text) -> None:
        self.text = text
        self._p1 = 0
        self._p2 = 0

    def read_id(self):


    def get_next_token(self):
        if self._p1 >= len(self.text):
            return 
        raw = ""
        char = self.text[self._p1]
        if char == "=":
            return 
        elif char in "a-zA-Z_":
            return 
        elif char in "0-9":
            return 
        elif char in "+-*/":
            return 
        elif char in " \n":
            return 