# Write function that reverses a list, preferably in place.


def reverse_list(lists):
    length = len(lists)
    for i in range(0, length//2):
        lists[i], lists[length-i-1] = lists[length-i-1], lists[i]
    return lists


# test
lis = [12, 45, 89, 97, 34, 22, 75, 62]
print(reverse_list(lis))
