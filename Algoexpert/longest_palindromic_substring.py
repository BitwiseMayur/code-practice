"""
Longest Palindromic Substring
Write a function that, given a string, returns its longest palindromic substring.
A palindrome is defined as a string that's written the same forward and backward. Note that single-character strings are palindromes.
You can assume that there will only be one longest palindromic substring.
Sample Input: string = "abaxyzzyxf"
Sample Output: "xyzzyx"

Solution:
How to tackle such a question, first we need to find the optimal solution. The optimal solution is to go through each character and then checking whether it starts a palindrome. There can be two cases here, for ex: "aba" and "abba" both are palindromes with odd and even characters, we need to consider both the cases at every iteration. 

Solution: As mentioned at every step we have to get the odd and even palindromes using the same function, this we have to keep in mind and compare both the values, whichever is greater, compare it again with the longest substring which we already have. As the question has already mentioned that single-character is also a palindrome, we need to set the default to first character as our result and then keep on updating it. 

Time O(n^2) | Space O(n)
Time = O(n) * (O(n/2) + O(n/2)) => O(n^2)
Space = As we are slicing the string, in the worst case we will end up creating new substring of the same length
"""

def longestPalindromeSubString(string):
    # Store the indexes and slice the string as final result
    longestSubString = [0, 1]

    # As we have alredy taken into account of the first character, start the loop with the second character.
    # For the getPalindromSubString as we have to pass the left of the i, better to start with 1 else it will error out as IndexError
    for i in range(1, len(string)):    # O(n)
        odd = getPalindromSubString(string, i-1, i+1)    # case 'aba' | O(n/2)
        even = getPalindromSubString(string, i-1, i)    # case 'abba'    | O(n/2)
        
        # As we are comparing two arrays, we have to get the max path using lambda
        longest = max(odd, even, key=lambda x: x[1] - x[0])
        longestSubString = max(longest, longestSubString, key=lambda x: x[1] - x[0])

    return string(longestSubString[0]: longestSubString[1])

def getPalindromSubString(string, leftIdx, rightIdx):
    while leftIdx >= 0 and rightIdx < len(string):
        if string[leftIdx] != string[rightIdx]:
            break
        leftIdx -= 1
        rightIdx += 1

    # As the leftIdx is already one place below, return the starting index of the palindrome substring
    return [leftIdx + 1, rightIdx]

