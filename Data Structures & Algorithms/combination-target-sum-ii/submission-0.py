class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(index, intermediary, cur_sum):
            if cur_sum == target:
                result.append(list(intermediary))
                return
            if cur_sum > target:
                return
            
            for i in range(index, len(candidates)):
                # Skip duplicates
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                intermediary.append(candidates[i])
                backtrack(i + 1, intermediary, cur_sum + candidates[i])
                intermediary.pop()
        result = []
        candidates.sort()
        backtrack(0, [], 0)
        return result
        