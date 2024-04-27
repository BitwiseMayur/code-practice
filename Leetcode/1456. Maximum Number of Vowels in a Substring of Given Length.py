"""
1456. Maximum Number of Vowels in a Substring of Given Length
"""

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        result = runningCount = sum([char in vowels for char in s[:k]]) # Understand sum()

        for i in range(k, len(s)):
            if s[i] in vowels:
                runningCount += 1
            if s[i-k] in vowels:
                runningCount -= 1
            
            result = max(result, runningCount)

        return result
