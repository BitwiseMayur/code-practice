"""
392. Is Subsequence
"""

# Two Pointers method
# Iterate over the large string and check whether the element match with the sub string, if yes then increment both else increment only the large string pointer. 
# At the end check whether the sub string pointer is equal to the length of the sub sequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sPointer = 0
        tPointer = 0

        while sPointer < len(s) and tPointer < len(t):
            if t[tPointer] == s[sPointer]:
                sPointer += 1
            tPointer += 1

        return sPointer == len(s)
