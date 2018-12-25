""" Write a function that takes a list of numbers, a starting base b1 and a target base b2 and interprets the list as a
number in base b1 and converts it into a number in base b2 (in the form of a list-of-digits). So for example [2,1,0] in
base 3 gets converted to base 8 as [2,5].
"""


def base_conversion(lists, base1, base2):
    result = []
    sum_num = 0
    length = len(lists)

    # checking for invalid case
    for num in lists:
        if num >= base1:
            print(f"The number is out of range of base-{base1} range")
            exit(0)

    # base1 to base2
    for i in range(length):
        sum_num += (lists[i] * pow(base1, length - i - 1))
    while sum_num >= base2:
        result.append(sum_num % base2)
        sum_num = sum_num // base2
    else:
        result.append(sum_num)
        result.reverse()

    return result


# test
li = [2, 1, 0]
b1 = 3
b2 = 8
print(base_conversion(li, b1, b2))
