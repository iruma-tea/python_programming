animal = 'cat'


def f():
    animal = 'dog'
    print('after:', animal)


f()
print('global:', animal)
