import datetime


def some_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        function = func(*args, **kwargs)
        end_time = datetime.datetime.now()
        return end_time - start_time

    return wrapper


@some_decorator
def sum_ab(a, b):
    return a + b


print(sum_ab(2, 10))
