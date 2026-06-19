# We need to do a BFS and count the shortest distance from all
# the rotten nodes at once, until all the fresh fruit are rotten,
# or we exhausted all the nodes.

class Solution:
    FRESH = 1
    ROTTEN = 2
    DIRECTIONS = [
        [-1, 0],
        [0, -1],
        [1, 0],
        [0, 1]
    ]

    def is_valid(self, x, y, grid) -> bool:
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == self.FRESH

    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Base case checks
        if not grid or len(grid) == 0:
            return -1

        # Count all the fresh fruit to keep count
        # At the same time add all the rotten fruit to the queue
        fresh_fruit = 0
        minutes = 0
        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == self.FRESH:
                    fresh_fruit += 1
                if grid[i][j] == self.ROTTEN:
                    queue.append((i, j))


        # Process the queue until empty or fresh fruit reach 0
        while len(queue) and fresh_fruit:
        # Do another loop to pop all rotten fruit from q and process them
            for _ in range(len(queue)):
                fruit_x, fruit_y = queue.popleft()
                for dx, dy in self.DIRECTIONS:
                    neighbor_x, neighbor_y = fruit_x + dx, fruit_y + dy
                    if self.is_valid(neighbor_x, neighbor_y, grid):
                        # Set all the neighbors as rotten
                        grid[neighbor_x][neighbor_y] = self.ROTTEN
                        # decrease the nr of fresh fruit
                        fresh_fruit -= 1
                        # Add them back to the Q
                        queue.append((neighbor_x, neighbor_y))
            # increase the minutes at the end of the loop
            minutes += 1

        return minutes if fresh_fruit == 0 else -1