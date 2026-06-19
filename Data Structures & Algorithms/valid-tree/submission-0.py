from enum import Enum

class State:
    NOT_VISITED = 0
    VISITING = 1
    VISITED = 2

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1: # a tree always has n-1 edges
            return False
        # convert to adj_list
        adj_list = {i:[] for i in range(n)}
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        state = [State.NOT_VISITED] * n
        # dfs with cycle detection
        def has_cycle(node, parent) -> bool:
            state[node] = State.VISITING
            for neighbor in adj_list[node]:
                # In undirected graphs it's possible to visit the parent, and that 
                # is not counted as a cycle
                if neighbor == parent:
                    continue
                if state[neighbor] == State.NOT_VISITED:
                    if has_cycle(neighbor, node):
                        return True
                else: # If it's visited or visiting then we have a cycle
                    return True
            state[node] = State.VISITED
            return False

        # if not all nodes have been explored, not valid tree
        return not has_cycle(0, -1) and all(s == State.VISITED for s in state)
