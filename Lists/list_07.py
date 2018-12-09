# Write three functions that compute the sum of the numbers in a list: using a for-loop, a while-loop and recursion.


def sum_with_while(lists):
    list_sum = 0
    i = 0
    while i < len(lists):
        list_sum += lists[i]
        i += 1
    return list_sum


def sum_with_for(lists):
    list_sum = 0
    for i in range(0, len(lists)):
            list_sum += lists[i]
    return list_sum


def sum_with_recursion(lists, i):
    if i == 0:
        return lists[0]
    else:
        return lists[i] + sum_with_recursion(lists, i-1)


# test
li = [15, 25, 31, 78, 3, 87, 35, 45]
print(sum_with_while(li))
print(sum_with_for(li))
print(sum_with_recursion(li, len(li)-1))
