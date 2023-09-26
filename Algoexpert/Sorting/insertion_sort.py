"""
Insertion Sort: 
Consider the first part as sorted i.e. first element is sorted then INSERT the next element to its place. Now we have 2 elements that are sorted, repeat the same.
Space: O(1) -> As this is done In place
Time: O(N**2) -> Not good
"""
def insertion_sort(array):
  for i in range(1, len(array)):
      j = i
      while j > 0 and array[j] < array[j-1]:
          array[j], array[j-1] = array[j-1], array[j]
          j -= 1

    return array
