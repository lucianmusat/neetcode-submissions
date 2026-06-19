class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # convert to adj list
        adj_list = {i:[] for i in range(n)}
        for edge, target in edges:
            adj_list[edge].append(target)
            adj_list[target].append(edge)
        explored = set()
        connected_components = 0

        # dfs function, explore and mark as explored
        
        def explore(node: int) -> None:
            if node in explored:
                return
            explored.add(node)
            for neighbor in adj_list[node]:
                explore(neighbor)

        # go through nodes 0..n and do a dfs on un-explored elements. Count nr of calls
        for node in range(n):
            if node not in explored:
                connected_components += 1
                explore(node)

        return connected_components
