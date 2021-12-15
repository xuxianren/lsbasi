PLUS = "PLUS"
INTEGER = "INTEGER"
EOF = "EOF"


class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value
    

    def __str__(self):
        return f"Token {self.type}: {self.value}"

class Interpreter:
    def __init__(self, text) -> None:
        self.text = text
        self.position = 0
        self.current_token = None

    def error(self):
        raise Exception("警告：错误的输入内容!")
    
    def get_next_token(self):
        text = self.text
        if self.position >= len(self.text):
            return Token(EOF, None)
        current_char = text[self.position]
        if str.isdigit(current_char):
            token = Token(INTEGER, int(current_char))
            self.position += 1
            return token
        if current_char == "+":
            token = Token(PLUS, current_char)
            self.position += 1
            return token
        self.error()
    
    def expr(self):
        left = self.get_next_token()
        opr = self.get_next_token()
        right = self.get_next_token()
        return left.value + right.value


def main():
    while True:
        try:
            text = input(">>>")
        except EOFError:
            break
        if not text:
            continue
        i = Interpreter(text)
        print(i.expr())

if __name__ == "__main__":
    main()
