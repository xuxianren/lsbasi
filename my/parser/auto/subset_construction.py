"""NFA->DFA
子集构造法
"""
from thompson import NFA


# 非空边
def get_edges_by_source(edges, node):
    return [edge for edge in edges if edge[0] == node and edge[2] != "ε"]


# 空边
def get_blank_edges_target(edges, node):
    return [edge[1] for edge in edges if edge[0] == node and edge[2] == "ε"]

# 一个节点的ε闭包
def eps_closure(node, edges):
    c = [node]
    i = 0
    visited = set()
    while i < len(c):
        node = c[i]
        i += 1
        if node in visited:
            continue
        visited.add(node)
        targets = get_blank_edges_target(edges, node)
        for target in targets:
            if target not in c:
                c.append(target)
    return c


def to_dfa(nfa: NFA):
    dfa_status = []
    dfa_edges = []
    edges = nfa.edges
    i = 0
    worklist = [(None, nfa.start, None)]
    while i < len(worklist):
        c = eps_closure(worklist[i][1], edges)
        try:
            index = dfa_status.index(c)
        except ValueError:
            index = len(dfa_status)
            dfa_status.append(c)
        if worklist[i][0] is not None:
            new_edge = [worklist[i][0], index, worklist[i][2]]
            if new_edge not in dfa_edges:
                dfa_edges.append(new_edge)
        for node in c:
            for edge in get_edges_by_source(edges, node):
                new_work = [index, edge[1], edge[2]] 
                if new_work not in worklist:
                    worklist.append([index, edge[1], edge[2]])
        i += 1
    return {"status": [(i, nfa.end in c) for i,c in enumerate(dfa_status)], "edges": dfa_edges}


if __name__ == "__main__":
    from parse import REParser
    from thompson import post2nfa
    # text = "a(b|c)*"
    text = "fee|fie"
    re = REParser(text)
    nfa = post2nfa(re.to_post())
    # print(nfa)
    print(to_dfa(nfa))