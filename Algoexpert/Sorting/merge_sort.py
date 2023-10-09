"""
Merge Sort:
Keep dividing the array into two parts and once it divides till the single element try to sort and merge it back. Check comments
"""
def mergeSort(array):
    if len(array) == 1:
        # mistake: writing 'return' only will return None, make sure to return the array
        return array
    
    midIdx = len(array) // 2
    return mergeSortHelper(mergeSort(array[:midIdx]), mergeSort(array[midIdx:]))

def mergeSortHelper(leftArray, rightArray):
    # Generate an empty list, else it will be a costly operation to append the element at the end
    sortedArray = [None] * (len(leftArray) + len(rightArray))
    k = i = j = 0
    
    while i < len(leftArray) and j < len(rightArray):
        if leftArray[i] < rightArray[j]:
            sortedArray[k] = leftArray[i]
            i += 1
        else:
            sortedArray[k] = rightArray[j]
            j += 1
        k += 1

    # Appending the remaining elements in the leftarray
    while i < len(leftArray):
        sortedArray[k] = leftArray[i]
        i += 1
        k += 1
        
    while j < len(rightArray):
        sortedArray[k] = rightArray[j]
        j += 1
        k += 1
        
    return sortedArray
