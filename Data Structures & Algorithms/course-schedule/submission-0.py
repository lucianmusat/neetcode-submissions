class Solution:

    def to_adj_list(self, numCourses: int, prerequisites: List[List[int]]):
        adj_list = {i:[] for i in  range(numCourses)}
        for c1, c2 in prerequisites:
            adj_list[c1].append(c2)
        return adj_list

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = self.to_adj_list(numCourses, prerequisites)
        visited = set()

        def has_cycle(node) -> bool:
            if node in visited or len(adj_list[node]) == 0:
                return False
            visited.add(node)
            for pq in adj_list[node]:
                if pq in visited or has_cycle(pq):
                    return True
            visited.remove(node)
            return False

        for node in adj_list:
            if has_cycle(node):
                return False
        return True