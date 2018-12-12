# Write a function that takes a number and returns a list of its digits. So for 2345 it should return [2,3,4,5].


def split_num(num):
    i = num
    lists = []
    while i >= 10:
        div = i // 10
        rem = i % 10
        i = div
        lists.append(rem)
    lists.append(i)
    lists.reverse()
    return lists


# test
number = 2345
print(split_num(number))
