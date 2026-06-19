from enum import Enum

class State(Enum):
    UNVISITED = 0
    VISITING = 1
    VISITED = 2

class Solution:
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 0 or prerequisites is None:
            return [] 

        adj_list = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            adj_list[course].append(pre)
        state = [State.UNVISITED] * numCourses
        solution = []
        has_cycle = False
        
        def dfs(course) -> bool:
            nonlocal has_cycle
            if state[course] == State.VISITING: # Cycle detected
                has_cycle = True 
                return
            if state[course] == State.VISITED:
                return
        
            state[course] = State.VISITING
            for neigh in adj_list[course]:
                dfs(neigh)
                if has_cycle:
                    return
            state[course] = State.VISITED
            solution.append(course)

        for course in range(numCourses):
            if state[course] == State.UNVISITED:
                dfs(course)
                if has_cycle:
                    return []

        return solution
        