class State(int):
    current = 0

    def __new__(cls):
        self = super().__new__(cls, cls.current)
        self.name = f"q{cls.current}"
        cls.current += 1
        return self

    def __str__(self) -> str:
        return self.name

x = State()
y = State()
print(y)