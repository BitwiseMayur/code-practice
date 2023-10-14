"""
For question refer find_three_largest_numbers.md
"""

# Time O(n) | Space O(1)
def findThreeLargestNumbers(array):
    result = [None] * 3

    for value in array:
        thirdLargest(result, value)
    return result

def thirdLargest(result, value):
    if result[2] is None or value > result[2]:
        shiftAndUpdate(result, value, 2)
    elif result[1] is None or value > result[1]:
        shiftAndUpdate(result, value, 1)
    elif result[0] is None or value > result[0]:
        shiftAndUpdate(result, value, 0)

def shiftAndUpdate(result, value, idx):
    for i in range(idx + 1):
        if i == idx:
            result[i] = value
        else:
            result[i] = result[i + 1]
