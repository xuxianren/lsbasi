from enum import Enum


class Token(Enum):
    EOF = -1
    
    ANY = 1
    AT_BOL = 2
    AT_EOL = 3
    CCL_END = 4
    CCL_START = 5
    CLOSE_CURLY = 6
    CLOSE_PAREN = 7
    CLOSURE = 8
    DASH = 9
    END_OF_INPUT = 10
    L = 11
    OPEN_CURLY = 12
    OPEN_PAREN = 13
    OPTIONAL = 14
    OR = 15
    PLUS_CLOSE = 16


Tokens = {
    '.': Token.ANY,
    '^': Token.AT_BOL,
    '$': Token.AT_EOL,
    ']': Token.CCL_END,
    '[': Token.CCL_START,
    '}': Token.CLOSE_CURLY,
    ')': Token.CLOSE_PAREN,
    '*': Token.CLOSURE,
    '-': Token.DASH,
    '{': Token.OPEN_CURLY,
    '(': Token.OPEN_PAREN,
    '?': Token.OPTIONAL,
    '|': Token.OR,
    '+': Token.PLUS_CLOSE,
}