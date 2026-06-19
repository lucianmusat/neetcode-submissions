class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Use a monotonic queue to keep track of the maximums
        # The queue is always in decreasing order
        queue = collections.deque()  # store indexes
        l = 0
        result = []

        for r in range(len(nums)):
            # pop all the smaller values from the queue
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            
            # add the next one to the queue
            queue.append(r)

            # ??
            if l > queue[0]:
                queue.popleft()

            # ??
            if r + 1 >= k:
                result.append(nums[queue[0]])
                l += 1
        
        return result
