from functools import wraps


def count_calls(func):
    """
    The count decorator is used to count the number of times a function has been called.
     This can be useful for profiling and optimization purposes.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f'{func.__name__} has been called: {wrapper.count}')
        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper
