l = ['Mon', 'tue', 'Web', 'Thu', 'Fri', 'sat', 'Sun']


def change_words(words, func):
    for word in words:
        print(func(word))


def sample_func(word):
    return word.capitalize()


def sample_func2(word):
    return word.lower()


change_words(l, sample_func)
change_words(l, sample_func2)
