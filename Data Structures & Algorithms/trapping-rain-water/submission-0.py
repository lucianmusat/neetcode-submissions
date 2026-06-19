# Basically it boils down to this: for each position the ammount
# of rain water we can hold is min(maxLeft, maxRight) - currentVal
# The smallest side edge - current height.
# formula: min(maxLeft, maxRigth) - height[i]
# Iterative solution is to do a pass and calculate the maxLeft and maxRight
# for each position and store in a separate vector, then do another pass
# and calculate the ammount of water for each position.
# Two pointer solution: we can do only one pass, we keep track for each
# of what is maxLeft and maxRight and narrow it down

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxLeft, maxRight = height[l], height[r]
        result = 0

        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                result += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                result += maxRight - height[r]

        return result 