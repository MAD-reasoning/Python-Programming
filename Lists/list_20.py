""" Write function that translates a text to Pig Latin and back. English is translated to Pig Latin by taking the first
letter of every word, moving it to the end of the word and adding ‘ay’.
“The quick brown fox” becomes “Hetay uickqay rownbay oxfay”.
"""


def pig_latin(sentence):
    result = ""
    lists = sentence.split()
    for index, item in enumerate(lists):
        result += item[1:] + item[0] + 'ay '
    return result


# test
line = "the quick brown fox"
print(pig_latin(line))
