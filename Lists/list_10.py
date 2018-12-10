# Write a function that combines two lists by alternatingly taking elements, e.g. [a,b,c], [1,2,3] → [a,1,b,2,c,3].


def concat(list1, list2):
    lists = []
    if len(list1) > len(list2):
        length = len(list1)
    else:
        length = len(list2)
    for i in range(0, length):
        if i < len(list1):
            lists.append(list1[i])
        if i < len(list2):
            lists.append(list2[i])
    return lists


# test
l1 = ["a", "b", "c"]
l2 = [1, 2, 3]
print(concat(l1, l2))
