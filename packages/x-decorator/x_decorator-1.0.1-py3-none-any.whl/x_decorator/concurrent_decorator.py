import concurrent.futures
from functools import wraps


def x_concurrent(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(func, *args, **kwargs)
            result = future.result()
        return result

    return wrapper
