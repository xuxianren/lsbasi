"""NFA->DFA
子集构造法
"""
from thompson import NFA, State, Edge

class Subset:
    total = []
    count = 0
    state_set = {}
    def __new__(cls, state, subset):
        for instance in cls.total:
            if instance.subset == subset:
                instance.nodes.append(state)
                cls.state_set[state] = instance
                return instance
        intance = super().__new__(cls)
        intance.state = [state]
        instance.subset = subset
        instance.count = cls.count
        cls.count += 1
        cls.state_set[state] = instance
        return instance
    

class SubsetConstruction:

    def __init__(self, nfa) -> None:
        self.nfa = nfa

    # 节点ε边的target
    def eps_targets(self, source):
        targets = []
        for edge in self.nfa.edges:
            if edge.source == source and edge.char == "":
                targets.append(edge.target)
        return targets

    # 节点非ε边的target
    def no_eps_targets(self):
        targets = []
        for edge in self.nfa.edges:
            if edge.source == source and edge.char != "":
                targets.append(edge.target)
        return targets

    # 一个节点的ε闭包
    def eps_closure(self, state):
        subset = [state]
        i = 0
        visited = []
        while i < len(subset):
            state = subset[i]
            i += 1
            if state in visited:
                continue
            visited.append(state)
            targets = self.eps_targets()
            for target in targets:
                if target not in subset:
                    subset.append(target)
        return subset

    def to_dfa(self):
        dfa_status = []
        dfa_edges = []

        # 所有节点的eps闭包
        for state in self.nfa.status:
            subset = self.eps_closure(state)
            Subset(state, subset)
        dfa_status = list(range(Subset.count))
        
        # 建立边
        no_eps_edges = [edge for edge in self.nfa.edges if edge["char"]]
        for edge in no_eps_edges:
            source = Subset.state_set[edge.source].id
            target = Subset.state_set[edge.target].id
            new_edge = Edge(source, target, edge.char)
            dfa_edges.append(new_edge)
        return {"status": dfa_status, "edges": dfa_edges}

class DFA:

    def __init__(self) -> None:
        self.status = []
        self.edges = []

if __name__ == "__main__":
    from parse import REParser
    from thompson import post2nfa
    # text = "a(b|c)*"
    text = "fee|fie"
    re = REParser(text)
    nfa = post2nfa(re.to_post())
    # print(nfa)
    print(to_dfa(nfa))