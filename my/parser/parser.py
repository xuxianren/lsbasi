from ..token import *

whitespace = ' \t\n\r\v\f'
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_letters = ascii_lowercase + ascii_uppercase
digits = '0123456789'

punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
printable = digits + ascii_letters + punctuation + whitespace

id_start = ascii_letters + "_"
id_content = ascii_letters + digits + "_"
operator = [
	"+",
	"-",
	"*",
	"/",
	"<",
	"<=",
	">",
	">=",
	"!=",
	"==",
]

KEY_WORLD = {
    "IF"
    
}

class Parser:


    def __init__(self, text) -> None:
        self.text = text
        self._p1 = 0
        self._p2 = 0

    def read_id(self):
        pass

    def get_identifier(self, ):
        pass
    
    def get_number(self, ):
        pass
    
    def get_oprator(self):
        pass

    def get_next_token(self):
        if self._p1 >= len(self.text):
            return 
        char = self.text[self._p1]
        if char in id_start:
            return self.get_identifier()
        elif char in digits:
            return self.get_number()
        elif char in operator:
            return self.get_oprator()
        elif char in whitespace:
            return self.get_next_token()