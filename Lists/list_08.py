""" Write a function on_all that applies a function to every element of a list. Use it to print the first twenty perfect
squares. The perfect squares can be found by multiplying each natural number with itself. The first few perfect squares
are 1*1= 1, 2*2=4, 3*3=9, 4*4=16. Twelve for example is not a perfect square because there is no natural number m so
that m*m=12. """


import math


def on_all(lists):
    result = []
    for i in range(0, len(lists)):
        if len(result) != 20:
            num = math.sqrt(lists[i])
            if int(num) == num and num != 0.0:
                result.append(int(num))
    return result


# test
li = [15, 25, 31, 78, 9, 87, 35, 45, 0, 15, 45, 35, 79, 36, 64, 4, 1, 81]
print(on_all(li))
