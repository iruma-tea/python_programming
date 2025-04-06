def print_func(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper


@print_func
def add_num(a, b):
    return a + b


r = add_num(10, 20)
print(r)
