# Write a function that returns the largest element in a list.


def largest_in_list(lists):
    num = lists[0]
    for i in range(0, len(lists)-1):
        if num < lists[i+1]:
            num = lists[i+1]
    return num


# test
li = [15, 25, 31, 78, 3, 87, 35, 45]
print(largest_in_list(li))
