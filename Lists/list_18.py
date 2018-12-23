# Implement binary search.


def binary_search(lists, num):
    begin, end = 0, len(lists)
    while begin <= end:
        mid = (begin + end) // 2
        if lists[mid] == num:
            return mid
        elif lists[mid] > num:
            end = mid - 1
        elif lists[mid] < num:
            begin = mid + 1
    return 'N/A'


# test
li = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
n = 21
print('The number is present at index: ', binary_search(li, n))
