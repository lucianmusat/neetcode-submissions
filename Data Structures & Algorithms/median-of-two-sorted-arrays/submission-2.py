class Solution:

    @staticmethod
    def sort_two_arrays(nums1: List[int], nums2: List[int]) -> List[int]:
        ret = []
        i, j = 0, 0
        # Check both vectors and zip them with the numbers in increasing order
        # using two pointers
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                ret.append(nums1[i])
                i += 1
            else:
                ret.append(nums2[j])
                j += 1
        # We might have leftover numbers in one of the original vectors
        # Let's continue where we left off and add the remaining numbers
        while i < len(nums1):
            ret.append(nums1[i])
            i += 1
        while j < len(nums2):
            ret.append(nums2[j])
            j += 1
        return ret
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Easy mode: nums = sorted(nums1 + nums2)
        nums = self.sort_two_arrays(nums1, nums2)
        n = len(nums)
        if n % 2 == 0:
            return (nums[n // 2 - 1] + nums[n // 2]) / 2
        else:
            return nums[n // 2]