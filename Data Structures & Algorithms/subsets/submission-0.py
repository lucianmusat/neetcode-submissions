class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(start, current_subset):
            # Add the current subset to the result
            result.append(list(current_subset))
            
            # Explore further subsets
            for i in range(start, len(nums)):
                # Add nums[i] to the current subset
                current_subset.append(nums[i])
                
                # Recur with the next element
                backtrack(i + 1, current_subset)
                
                # Backtrack: Remove nums[i] from the subset
                current_subset.pop()
        
        result = []
        backtrack(0, [])
        return result