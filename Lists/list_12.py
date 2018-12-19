# Write a function that rotates a list by k elements. For example [1,2,3,4,5,6] rotated by two becomes [3,4,5,6,1,2].
# Try solving this without creating a copy of the list.


def rotates(lists, r):
    for i in range(0, r):
        temp = lists.pop(0)
        lists.append(temp)
    return lists


# test
li = [1, 2, 3, 4, 5, 6]
ro = 2
print(rotates(li, ro))
