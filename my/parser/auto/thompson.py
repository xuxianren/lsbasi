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
import sys
sys.path.append(r"D:\projects\compiler\lsbasi")
import json
from my.render import render
from parse import REParser, CONNECT, OR, KLEENE


class State(int):
    current = 0

    def __new__(cls):
        self = super().__new__(cls, cls.current)
        self.label = f"q{cls.current}"
        cls.current += 1
        return self

    def to_dict(self):
        return {"id": self, "label": self.label}

    def __str__(self) -> str:
        return self.label

class Edge:
    def __init__(self, source, target, char) -> None:
        self.source = source
        self.target = target
        self.char = char
        self.label = char if char else "ε"

    def to_dict(self):
        return {
            "source": self.source, 
            "target": self.target,
            "label": self.label,
        }

class NFA:
    count = 0

    def newState(self):
        state = self.__class__.count
        self.__class__.count += 1
        self.status.add(state)
        return state

    def __init__(self, char="") -> None:
        self.start = State()
        self.end = State()
        self.status = [self.start, self.end]
        edge = Edge(self.start, self.end, char)
        self.edges = [edge]

    def _merge(self, other):
        self.status.extend(other.status)
        self.edges.extend(other.edges)

    def connect(self, other):
        self._merge(other)
        self.edges.append(Edge(self.end, other.start, "ε"))
        self.end = other.end

    def oor(self, other):
        self._merge(other)
        start = State()
        end = State()
        self.edges.append(Edge(start, self.start, ""))
        self.edges.append(Edge(start, other.start, ""))
        self.edges.append(Edge(self.end, end, ""))
        self.edges.append(Edge(other.end, end, ""))
        self.start = start
        self.end = end
    
    def kleene(self):
        start = State()
        end = State()
        self.edges.append(Edge(start, self.start, ""))
        self.edges.append(Edge(self.end, end, ""))
        self.edges.append(Edge(self.end, self.start, ""))
        self.edges.append(Edge(start, end, ""))
        self.start = start
        self.end = end

    def __dict__(self):
        data = {"nodes": [], "edges": []}
        for node in self.status:
            data["nodes"].append(node.to_dict())
        for edge in self.edges:
            data["edges"].append(edge.to_dict())
        return data
        
    def json(self):
        return json.dumps(self.__dict__())

    def __str__(self) -> str:
        return self.json()

def post2nfa(post):
    stack = []
    for token in post:
        if token.t == CONNECT:
            n2 = stack.pop()
            stack[-1].connect(n2)
        elif token.t == OR:
            n2 = stack.pop()
            stack[-1].oor(n2)
        elif token.t == KLEENE:
            stack[-1].kleene()
        else:
            stack.append(NFA(token.v))
    if stack:
        return stack[-1]
    else:
        return NFA("")

def main():
    text = "f(ee|ie)*"
    re = REParser(text)
    nfa = post2nfa(re.to_post())
    render(nfa.__dict__())

if __name__ == "__main__":

    main()