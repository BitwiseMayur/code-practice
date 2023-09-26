"""
Remove Duplicate Letters: From Leetcode
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is 
the smallest in lexicographical order among all possible results.

Example 1:
Input: s = "bcabc"
Output: "abc"

Example 2:
Input: s = "cbacdcbc"
Output: "acdb"
"""
def removeDuplicateLetters(self, s: str) -> str:
    counter, seen, stack = [0] * 26, [False] * 26, []
    for char in s:
        counter[ord(char) - ord('a')] += 1
    
    for char in s:
        index = ord(char) - ord('a')
        counter[index] -= 1
        if seen[index]:
            continue
        while stack and char < stack[-1] and counter[ord(stack[-1]) - ord('a')]:
            seen[ord(stack.pop()) - ord('a')] = False
        stack.append(char)
        seen[index] = True
    
    return ''.join(stack)
