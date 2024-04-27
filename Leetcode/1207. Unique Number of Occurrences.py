"""
1207. Unique Number of Occurrences
"""
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        num_occ = {}

        for item in arr:
            num_occ[item] = num_occ.get(item, 0) + 1

        return len(num_occ) == len(set(num_occ.values()))
