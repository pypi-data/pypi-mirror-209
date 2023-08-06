import time
from functools import wraps


def timing(func):
    """
    used to measure the time it takes for a function to execute.

    EX:

    @timing_decorator
    def my_function():
        # some code here
        time.sleep(1)  # simulate some time-consuming operation
        return
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.monotonic()
        result = func(*args, **kwargs)
        end_time = time.monotonic()
        print(f"{func.__name__} took {end_time - start_time:.2f} seconds to run.")
        return result

    return wrapper
