"""
Bubble sort implementation
"""
def bubbleSort(array):
    n = len(array)
    sorted = False
    while not sorted:
        sorted = True
        for i in range(n - 1):
            if array[i] > array[i+1]:
                # swap
                array[i], array[i+1] = array[i+1], array[i]
                sorted = False
        n -=1
    return array
