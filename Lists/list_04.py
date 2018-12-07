# Write a function that returns the elements on odd positions in a list.


def occur(lists):
    list_1 = []
    for i in range(0, len(lists)):
        if i % 2 == 0:
            list_1.append(lists[i])
    return list_1


# test
lis = [0, 2, 45, 78, 65, 32, 66]
print(occur(lis))
