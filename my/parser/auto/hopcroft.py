"""最小化DFA
"""
'''
//基于等价类的思想
split(S)
    foreach(character c)
        if(c can split s)
            split s into T1, ..., Tk

hopcroft()
    split all nodes into N, A
    while(set is still changes)
        split(s)
'''

# dfa = {"nodes": [(0, False), (1, True)], "edges": [(0, 1, "a")]}


class Hopcroft:
    def __init__(self, dfa) -> None:
        self.dfa = dfa
        n = [node[0] for node in dfa["nodes"] if not node[1]]
        a = [node[0] for node in dfa["nodes"] if node[1]]
        self.S = [n, a]

    def get_chars(self, s):
        return [edge[2] for edge in self.dfa["edges"] if edge[0] in s]

    def get_target(self, source, char):
        for edge in self.dfa["edges"]:
            if edge[0] == source and edge[2] == char:
                return edge[1]

    def find_set(self, node):
        for i, s in enumerate(self.S):
            if node in s:
                return i

    def find_t(self, node):


    def split(self, s):
        subs = {}
        for char in self.get_chars(s):
            for node in s:
                target = self.get_target(node, char)
                if target is not None:
                    target_set = self.find_set(target)
                    if target_set in subs:
                        if node not in subs[target_set]:
                            subs[target_set].append(node)
                    else:
                        subs[target_set] = [node]
        return subs.values()

    def h(self):
        while True:
            i = 0
            while i < len(self.S):
                s = self.S[i]
                subs = self.split(s)
                if len(subs) > 1:
                    self.S.pop(i)
                    self.S.extend(subs)
                    break
                i += 1
            else:
                break
    
    def new_dfa(self):
        class Nodes:
            
        node = 0
        nodes = []
        edges = []
        visited= []
        for s in self.S:
            if node in s:
                try:
                    state = visited.index(s)
                except ValueError:
                    state = len(visited)
                    visited.append(s)
                    nodes.append(state)


                nodes.append[]
                self.
            

if __name__ == "__main__":
    dfa = {
        'nodes': [(0, False), (1, False), (2, False), (3, False), (4, False),
                   (5, True), (6, True)],
        'edges': [[0, 1, 'f'], [0, 2, 'f'], [1, 3, 'e'], [2, 4, 'i'],
                  [3, 5, 'e'], [4, 6, 'e']]
    }
    h = Hopcroft(dfa)
    h.h()
    print(h.S)