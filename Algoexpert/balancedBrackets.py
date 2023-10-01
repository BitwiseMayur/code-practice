"""
Balanced Brackets

Given a string, we have to identify whether the brackets in the string are balanced. It is said to be balanced when,
1. the number of opening and closing brackets are same and in order
2. '[(])' is not considered to be balanced, '[()]' is considered balanced.
3. '{2}[]' is also considered as balanced

Initially I thought, is there any builtin function that exists to check whether the character is a bracket like isnum, there is none. We have to create both open and closed brackets objects.

Make sure to check whether the final stack is empty
"""

#  O(N) time and O(1) space
def balancedBrackets(string):
    brackets_stack = []

    #  Create objects to same index for open and close brackets
    open_brackets = {'(':0, '[': 1, '{':2, '<':3}
    closed_brackets = {')':0, ']': 1, '}':2, '>':3}

    for bracket in string:
        if bracket in open_brackets:
            brackets_stack.append(open_brackets[bracket])
        elif bracket in closed_brackets:
            if not brackets_stack or closed_brackets[bracket] != brackets_stack.pop():
                return False
    
    return len(brackets_stack) == 0
