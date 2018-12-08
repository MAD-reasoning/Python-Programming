# Write a function that computes the running total of a list.


def sum_of_list(lists):
    list_sum = 0
    for i in range(0, len(lists)):
            list_sum += lists[i]
    return list_sum


# test
lis = [0, 2, 45, 78, 65, 32, 66]
print(sum_of_list(lis))
