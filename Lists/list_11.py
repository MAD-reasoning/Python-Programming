# Write a function that merges two sorted lists into a new sorted list. [1,4,6],[2,3,5] → [1,2,3,4,5,6].
# You can do this quicker than concatenating them followed by a sort.


def concat(list1, list2):
    lists = []
    j, k = 0, 0
    length = len(list1) + len(list2) - 1
    for i in range(0, length):
        if len(list1) > j:
            print("a")
            if list1[j] > list2[k]:
                lists.append(list1[j])
                j += 1
                print('b')
        if len(list2) > k:
            print('c')
            if list1[j] < list2[k]:
                lists.append(list2[k])
                k += 1
                print("d")
    return lists


# test
l1 = [1, 4, 6]
l2 = [2, 3, 5]
print(concat(l1, l2))
