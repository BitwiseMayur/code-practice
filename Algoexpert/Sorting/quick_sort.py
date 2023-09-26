"""
Quick sort implementation: (DAC- Divide and Conquer)

Set a pivot as the first element, the intention is to get to the Pivot's actual place in the array then the array will be divided into 2 parts. Left and Right of Pivot we apply the same logic. To get to the right place, compare L and R's value with the Pivot. The end goal is to move all the lesser elements to the Left of Pivot and the greater ones to the right side and repeat.
"""

def quickSort(array):
    quickSortOperation(array, 0, len(array) - 1)
    return array
    
def quickSortOperation(array, firstIdx, lastIdx):
    if firstIdx >= lastIdx:
        return
    pivot = array[firstIdx]
    leftP = firstIdx + 1
    rightP = lastIdx
    

    while rightP >= leftP:
        if array[rightP] < pivot and array[leftP] > pivot:
            array[rightP], array[leftP] = array[leftP], array[rightP]
        if array[rightP] >= pivot:
            rightP -= 1
        if array[leftP] <= pivot:
            leftP += 1

    array[rightP], array[firstIdx] = array[firstIdx], array[rightP]
    leftsmaller = rightP - 1 - firstIdx < lastIdx - (rightP + 1)
    if leftsmaller:
        quickSortOperation(array, firstIdx, rightP -1)
        quickSortOperation(array, rightP + 1, lastIdx)
    else:
        quickSortOperation(array, rightP + 1, lastIdx)
        quickSortOperation(array, firstIdx, rightP -1)
