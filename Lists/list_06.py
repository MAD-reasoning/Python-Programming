# Write a function that tests whether a string is a palindrome.


def reverse_list(strings):
    rev = []
    length = len(strings)
    for i in range(0, length):
        rev.append(strings[length - i - 1])
    return rev


def is_palindrome(words):
    lists_rev = reverse_list(words)
    lists = reverse_list(lists_rev)
    print("Is palindrome...")
    if lists == lists_rev:
        return True
    return False


# test
st = "sagas"
print(is_palindrome(st))
