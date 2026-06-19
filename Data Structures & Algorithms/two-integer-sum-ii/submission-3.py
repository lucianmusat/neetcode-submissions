class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            num_sum = numbers[l] + numbers[r]
            print(f"Checking {l} and {r}, sum: {num_sum}")
            if num_sum == target:
                return [l + 1, r + 1]
            elif num_sum < target:
                l += 1
            else:
                r -= 1