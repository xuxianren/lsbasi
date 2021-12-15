INTEGER = 'INTEGER'
PLUS = 'PLUS'
MINUS = 'MINUS'
MUL = 'MUL'
DIV= 'DIV'
EOF= 'EOF'


class Token:
    def __init__(self, name, raw) -> None:
        self.name = name
        self.raw = raw
        self.value = raw
        
        self.set_value()
    

    def set_value(self):
        if self.name == INTEGER:
            self.value = int(self.raw)