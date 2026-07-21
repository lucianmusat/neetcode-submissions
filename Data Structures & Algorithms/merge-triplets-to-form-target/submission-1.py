class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for t in triplets:
            # if any element in current triplet is greater than the target at the
            # same index, we can't use it, so ignore
            if any(t[i] > target[i] for i in range(3)):
                continue
            
            # Any of the position is the correct value we need?
            # Then it's possible to generate the partial solution using this
            # because it is guaranteed that the remaining triplets are <= target
            for i, v in enumerate(t):
                if v == target[i]: 
                    good.add(i)
            
        return len(good) == 3
