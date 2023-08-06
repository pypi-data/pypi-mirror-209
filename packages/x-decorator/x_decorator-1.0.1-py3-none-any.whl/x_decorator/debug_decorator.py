from functools import wraps


def debug(func):
    """
    The debug decorator is used to print debugging information about the function calls.
     This can be useful during development and testing.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__} with args: {args}, kwargs: {kwargs}')
        result = func(*args, **kwargs)
        print(f'Result of {func.__name__}: {result}')
        return result

    return wrapper
