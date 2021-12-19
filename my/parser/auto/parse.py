"""
支持
a-zA-Z0-9

a|b
ab
a*

\
(), (?:), (?=), []
*, +, ?, {n}, {n,}, {n,m}
^, $, \任何元字符、任何字符
|
"""

from os import stat
import string
whitespace = ' \t\n\r\v\f'
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_letters = ascii_lowercase + ascii_uppercase
digits = '0123456789'
hexdigits = digits + 'abcdef' + 'ABCDEF'
octdigits = '01234567'
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
printable = digits + ascii_letters + punctuation + whitespace

table = string.ascii_letters + string.digits

alpha = string.ascii_letters + string.digits
opr = "|*"
text = "ab|c"

# 基础类型
BLANK = "blank"
CHAR = "char"

# 括号
LEFT_BRACKET = "left_bracket"
RIGHT_BRACKET = "right_bracket"

# 操作
OR = "or"
CONNECT = "connect"
KLEENE = "kleene"

def cmp_opr(token1, token2):
    orders = [OR, CONNECT, KLEENE]
    return orders.index(token1.t) - orders.index(token2.t)




class Token:
    def __init__(self, t, v) -> None:
        self.t = t
        self.v = v
    
    def __str__(self) -> str:
        return f"{self.t}: {self.v}"



class REParser:
    def __init__(self, text) -> None:
        self.text = text
        self._index = 0
    
    def _get_token(self):
        while self._index < len(self.text):
            char = self.text[self._index]
            self._index += 1
            if char == "*":
                yield Token(KLEENE, "*")
            elif char == "|":
                yield Token(OR, "|")
            elif char == "(":
                yield Token(LEFT_BRACKET, "(")
            elif char == ")":
                yield Token(RIGHT_BRACKET, ")")
            else:
                yield Token(CHAR, char)

    def get_token(self):
        yield from self._get_token()

    def add_connect(self):
        last_token = None
        for token in self.get_token():
            if token is None:
                break
            if token.t in (CHAR, LEFT_BRACKET):
                if last_token and last_token.t in (CHAR, RIGHT_BRACKET):
                    yield Token(CONNECT, "-")
            yield token
            last_token = token

    def to_post(self):
        stack = []
        result = []
        for token in self.add_connect():
            if token.t == CHAR:
                result.append(token)
            elif token.t == LEFT_BRACKET:
                stack.append(token)
            elif token.t == RIGHT_BRACKET:
                while True:
                    token = stack.pop()
                    if token.t == LEFT_BRACKET:
                        break
                    result.append(token)
            else:
                while True:
                    if not stack or stack[-1].t == LEFT_BRACKET or cmp_opr(token, stack[-1])>0:
                        stack.append(token)
                        break
                    else:
                        result.append(stack.pop())
        if stack:
            stack.reverse()
            result.extend(stack)
        return result

if __name__ == "__main__":

    text = "a(b|c)*"
    t = REParser(text)
    result = t.to_post()
    print([token.v for token in result])