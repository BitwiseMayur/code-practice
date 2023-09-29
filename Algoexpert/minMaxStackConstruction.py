"""
Implementation of Min Max Stack Construction

The main agenda here is to implement the usual stack class along with a mechanism to get the minimim and maximum of the stack which runs in O(1) time complexity all the time. 
First thing that comes to the mind is to use builtin min() and max() over the list of all the stack objects, however this will run in O(n) to get the min and max. 

I tried to solve it with intializing two variables which hold min and max. For ex: self.min and self.max, let's say we have an array [5, 7, 2] currently we hold min as 2, suppose the 2 is popped to calculate the min we have to loops through the entire list again which is a costly operation. 

To solve this, we can use another minMaxStack array which holds the value of both min and max along with the actual stack array. At any given point we have the min and max values using this implementation. 
stack = []    minMaxStack = []
stack = [5]    minMaxStack = [{"min":5, "max":5}]
stack = [5, 7]    minMaxStack = [{"min":5, "max":5}, {"min":5, "max":7}]
stack = [5, 7, 2]    minMaxStack = [{"min":5, "max":5}, {"min":5, "max":7}, {"min":2, "max":7}]
Now when we pop 2, we got to pop the last element from the minMaxStack as well and the min and max values are kinda restored
stack = [5, 7]    minMaxStack = [{"min":5, "max":5}, {"min":5, "max":7}]
"""

class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.minMaxStack = []

    def peek(self):
        #  In a real case scenario we have to check wether the self.stack is non empty else we get a list out of index error
        return self.stack[-1] if self.stack else None

    def pop(self):
        if not self.stack:
            return None

        self.minMaxStack.pop()
        return self.stack.pop()

    def push(self, number):
        newMinMax = {"min":number, "max":number}
        if self.minMaxStack:
            currentMinMax = self.minMaxStack[-1]
            newMinMax["min"] = min(currentMinMax["min"], number)
            newMinMax["max"] = max(currentMinMax["max"], number)

        self.minMaxStack.append(newMinMax)
        self.stack.append(number)

    def getMin(self):
        if not self.minMaxStack:
            return None
        return self.minMaxStack[-1]["min"]

    def getMax(self):
        if not self.minMaxStack:
            return None
        return self.minMaxStack[-1]["max"]
        
