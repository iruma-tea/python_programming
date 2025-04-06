l = ['Mon', 'tue', 'Wed', 'Thu', 'Fri', 'sat', 'Sun']


def change_world(words, func):
    for word in words:
        print(func(word))


def sample_func(word):
    return word.capitalize()


change_world(l, sample_func)
