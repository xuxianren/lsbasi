"""RE->NFA
"""


"""
空串
空集
或
连接
闭包

a(a|b|c)*
基础
e -> {}
e -> {e}
a -> {a}
...

| u *

A|B = {x|x属于A或者属于B}
AB = {xy|x属于A且y属于B}
A+ = {}

语法糖

优先级
\
(), (?:), (?=), []
*, +, ?, {n}, {n,}, {n,m}
^, $, \任何元字符、任何字符
|


比如a|food表示a 或者 food
"""
import json

class NFA:
    count = 0

    @classmethod
    def newState(cls):
        state = cls.count
        cls.count += 1
        return state

    def __init__(self, char) -> None:
        if char == "":
            state = self.newState()
            self.start = state
            self.end = state
        else:
            self.start = self.newState()
            self.end = self.newState()
        self.status = {self.start, self.end}
        self.edges = {(self.start, self.end, char)}
    
    def merge(self, other):
        self.status |= other.status
        self.edges |= other.edges       

    def connect(self, other):
        self.merge(other)
        self.edges.add((self.end, other.start, ""))
        self.end = other.end

    def oor(self, other):
        self.merge(other)
        start = self.newState()
        end = self.newState()
        self.edges.add((start, self.start, ""))
        self.edges.add((start, other.start, ""))
        self.edges.add((self.end, end, ""))
        self.edges.add((other.end, end, ""))
        self.start = start
        self.end = end
    
    def xxr(self):
        start = self.newState()
        end = self.newState()
        self.edges.add((start, self.start, ""))
        self.edges.add((self.end, end, ""))
        self.edges.add((self.end, self.start, ""))
        self.edges.add((start, end, ""))
        self.start = start
        self.end = end

    def __str__(self) -> str:
        return json.dumps({"nodes": list(self.status), "edges": list(self.edges)})

def main():
    n = NFA("")
    n.connect(NFA("a"))
    n.connect(NFA("b"))
    print(n)
    print(n.accept("ab"))


if __name__ == "__main__":
    main()