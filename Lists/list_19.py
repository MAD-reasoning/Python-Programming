""" Write a function that takes a list of strings an prints them, one per line, in a rectangular frame.
 For example the list ["Hello", "World", "in", "a", "frame"] gets printed as:
 @@@@@@@@@
 @ Hello @
 @ World @
 @  in   @
 @   a   @
 @ frame @
 @@@@@@@@@
"""


def biggest(lists):
    temp = ''
    for i in lists:
        if len(temp) < len(i):
            temp = i
    return len(temp)


def word_frame(lists):
    length = biggest(lists)
    print('@@' + '@' * length + '@@')
    for i in lists:
        space_1, space_2 = ' ', ' '
        if len(i) < length:
            j = length - len(i)
            space_1 = space_1 + ' ' * (j // 2)
            space_2 = space_2 + ' ' * (j - j // 2)
        print('@' + space_1 + i + space_2 + '@')
    print('@@' + '@' * length + '@@')


# test
li = ["Hello", "World", "in", "a", "frame"]
word_frame(li)
