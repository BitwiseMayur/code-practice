"""
Write a function which gets a string as an input and returns the first non repeating character index, else return -1.
Ex: string = "abcdac"
Output = 1, as 'b' is the first non repeating character
"""

# Time O(n) | Space O(1)
def firstNonRepeatingCharacter(string):
    map_char = {}
    for char in string:
        if map_char.get(char):
            map_char[char] += 1
        else:
            map_char[char] = 1

    for idx in range(len(string)):
        if map_char[string[idx]] == 1:
            return idx
    return -1

# If the input is restricted to lowercase alphabets then the space complexity can have max of 26 elements which then becomes constant space operation O(1)
# If the input can be anything then it becomes O(n) operation
