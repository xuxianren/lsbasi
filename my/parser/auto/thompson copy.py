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
from parse import REParser, CONNECT, OR, KLEENE

class NFA:

    def __init__(self) -> None:
        pass

    count = 0

    def newState(self):
        state = self.__class__.count
        self.__class__.count += 1
        self.status.add(state)
        return state

    def __init__(self, char) -> None:
        self.status = set()
        self.edges = set()
        self.start = self.newState()
        self.end = self.newState()
        self.edges.add((self.start, self.end, char))

    
    def merge(self, other):
        self.status |= other.status
        self.edges |= other.edges       

    def connect(self, other):
        self.merge(other)
        self.edges.add((self.end, other.start, "ε"))
        self.end = other.end

    def oor(self, other):
        self.merge(other)
        start = self.newState()
        end = self.newState()
        self.edges.add((start, self.start, "ε"))
        self.edges.add((start, other.start, "ε"))
        self.edges.add((self.end, end, "ε"))
        self.edges.add((other.end, end, "ε"))
        self.start = start
        self.end = end
    
    def kleene(self):
        start = self.newState()
        end = self.newState()
        self.edges.add((start, self.start, "ε"))
        self.edges.add((self.end, end, "ε"))
        self.edges.add((self.end, self.start, "ε"))
        self.edges.add((start, end, "ε"))
        self.start = start
        self.end = end

    def to_json(self):
        data = {"nodes": [], "edges": []}
        for node in self.status:
            data["nodes"].append({
                "id": node, 
                "label": f"q{node}",
                "style": "fill:#ffffff00;stroke:red;" if node == self.end else "fill:#ffffff00;stroke:#000;"
            })
        for edge in self.edges:
            data["edges"].append({
                "source": edge[0],
                "target": edge[1],
                "label": edge[2],
            })
        return data

    def __str__(self) -> str:
        return json.dumps(self.to_json())

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
    text = "a(b|c)*"
    re = REParser(text)
    nfa = post2nfa(re.to_post())
    print(nfa)

if __name__ == "__main__":
    main()