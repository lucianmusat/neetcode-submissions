class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # append the target at the end with cost 0
        cost.append(0)

        # start backwards and compute the cost for each step
        # skip the target cell and skip the one before it because
        # that one's cost stays the same.
        for cell in range(len(cost) -3, -1, -1):
            cost[cell] += min(cost[cell + 1], cost[cell + 2])
        # The cost has been calculated for each cell, we need to
        # return which is the starting cell, first or second.
        return min(cost[0], cost[1])