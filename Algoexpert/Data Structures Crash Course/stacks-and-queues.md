Stacks and Queues

To understand the concept of Stacks, we can consider a real life example such as A stack of books placed on a table which I never read in my case! Here the books placed on top of one another is a representation of a stack(that's why it is called as a stack of books Duh'). The first book will be taken out first, it follows LIFO principle meaning Last In First Out. A new book can be added at the top and the same book has to be removed. This is a simple explanation of a Stack.

For Queue, off course we all know what a queue is, it's the same here as well. Queue is nothing but standing in line in a movie theatre for the expensive popcorn. First guy enters the queue gets it first and the last guy gets it at the very last in an ideal scenario unless you start a new line and confuse others. Queues follow FIFO principle meaning First In First Out. 

Time and Space complexity
It is a constant space and time operation to insert and remove an element from the stacks and queue.
O(1) - ST -> INSERT and DELETE

Consider a basic implementation of a stack, it is nothing but a dynamic array, for ex: [1, 2, 3]. 
If we want to add an element in the end, it is an amortized(explained this in Arrays) constant time operation. To add and remove an element at the end is a constant time operation. Regarding space, we will not use any additional space which is not intended apart from the array. Insertion and Deletion of an element in a stack is called as push and ~~pull~~ pop operations

For Queue, the basic implementation is not an array but a Linked list i.e "1 -> 2 -> 3 -> null" where we need to know the head and the tail of the linked list.
If we want to add the element, we just replace the head and for removal we delete the tail. Insertion and Deletion of a queue is called as enqueue and dequeue respectively.
