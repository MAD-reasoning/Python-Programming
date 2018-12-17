# Write a function that merges two sorted lists into a new sorted list. [1,4,6],[2,3,5] → [1,2,3,4,5,6].
# You can do this quicker than concatenating them followed by a sort.


def concat(list1, list2):
    lists = [item for item in list1]
    lists += [item for item in list2]
    lists.sort()
    return lists


# test
l1 = [1, 4, 6]
l2 = [2, 3, 5]
print(concat(l1, l2))
