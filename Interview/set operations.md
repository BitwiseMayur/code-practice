# 1. Union - |
Union of two sets gets you a set containing all the unique elements from both sets. You can use | or the union() method.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # Using the | operator
or
union_set = set1.union(set2)  # Using the union() method
print(union_set)  # Output: {1, 2, 3, 4, 5}
```


# 2. Intersection - &
Intersection of two sets gets you a set of elements common to both. Use & or the intersection() method.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1 & set2  # Using the & operator
or
intersection_set = set1.intersection(set2)  # Using the intersection() method
print(intersection_set)  # Output: {3}
```


# 3. Difference -
Difference of two sets returns elements that are in the first set but not in the second. Use - or the difference() method.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1 - set2  # Using the - operator
or
difference_set = set1.difference(set2)  # Using the difference() method
print(difference_set)  # Output: {1, 2}
```


# 4. Symmetric Difference - ^
Symmetric difference returns elements in either of the sets but not in both. Use ^ or the symmetric_difference() method.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
symmetric_difference_set = set1 ^ set2  # Using the ^ operator
\# or
symmetric_difference_set = set1.symmetric_difference(set2)  # Using the symmetric_difference() method
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}
```
