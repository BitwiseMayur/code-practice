"""
Selection Sorting
Let's say you have an unordered array, set the first value as minimum, then iterate from the second element and check whether it is smaller than the first. We will be having the minimum value at the end, replace that with the first element and do the same again and again.

Time complexity = O(N^2) As we have to implement 2 for/while loops and everytime the inner loop is reduced by one. 
Space complexity - O(1) As we are doing everything in place
"""
def selectionSort(array):
    
    for idx in range(len(array)):
        min = idx
        for j in range(idx+1, len(array)):
            if array[j] < array[min]:
                min = j

        array[idx], array[min] = array[min], array[idx]

    return array
