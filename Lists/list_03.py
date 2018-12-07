# Write a function that checks whether an element occurs in a list.


def occur(lists, element):
    for i in range(0, len(lists)):
        if lists[i] == element:
            return True
    return False


# test
lis = [0, 2, 45, 78, 65, 32, 66]
ele = 7
print(occur(lis, ele))
