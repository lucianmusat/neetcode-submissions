from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # transform times to adjacency list
        # priority queue sorts based on first element of the tuple, so we have to pass
        # the weight first
        adj_list = defaultdict(list)
        for ui, vi, ti in times:
            adj_list[ui].append((ti, vi))
        
        # priority queue
        q = []
        visited = set()
        # the result is the largest number of steps that actually reaches a node
        max_time = 0
        
        # insert starting element k into the priority queue
        heapq.heappush(q, (0, k))

        while q:
            weight, element = heapq.heappop(q)
            if element in visited:
                continue
            visited.add(element)
            
            max_time = max(max_time, weight)

            for next_weight, neighbor in adj_list[element]:
                heapq.heappush(q, (weight + next_weight, neighbor))
        
        return max_time if len(visited) == n else -1
