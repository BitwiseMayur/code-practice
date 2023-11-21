"""
Finding the loop in a singly Linked List
This is one of the interesting solution I have come across. Initially I thought I will solve this using dictionary, add the id as the key and the linked list node as the value and check if the id exists and it works as well. However to solve this using two pointers is something we should concentrate in this scenario. 

When we move using two pointers, first being moved one place at a time and second one at the twice of its speed
first = head.next
second = head.next.next

Both the pointers will meet at a point and we will stop the while loop here.
First = X distance
Second = 2X distance

head -> start of the loop = D
start of the loop -> meeting point = P
remaing = R

X = D + P
2X = 2D + 2P

Total distance of the linked list = Total distance travelled by second pointer - the extra distance covered by it = 2D + 2P - P
Total distance of the linked list = 2D + P

T = D + P + R
R = 2D + P - D - P
R = D -> This is it

So now we move back the first pointer to the head and keep the second one at the meeting point and move both the pointers at the same pace, we will reach at the starting point of the loop
"""

# Time O(N) | Space O(1)
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
    first = head.next
    second = head.next.next
    while first != second:
        first = first.next
        second = second.next.next

    first = head
    while first != second:
        first = first.next
        second = second.next

    return first
