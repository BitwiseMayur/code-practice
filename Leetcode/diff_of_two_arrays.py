"""
2215. Find the Difference of Two Arrays
"""
# My solution
from collections import defaultdict

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_map = defaultdict(int)
        nums2_map = defaultdict(int)
        result1 = set()
        result2 = set()

        for item in nums1:
            nums1_map[item] += 1

        for item in nums2:
            nums2_map[item] += 1

        for item in nums1:
            if nums2_map.get(item):
                continue
            if item not in result1:
                result1.add(item)

        for item in nums2:
            if nums1_map.get(item):
                continue
            if item not in result2:
                result2.add(item)

        return [list(result1), list(result2)]

# Use set operations
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        result1 = set1 - set2
        result2 = set2 - set1

        return [list(result1), list(result2)]
