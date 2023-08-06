from functools import wraps


def memoize(func):
    """
    Some parts of our codebase rarely change their behaviors.
     Yet, it may take a big chunk of our computation power. In such situations,
      we can use a decorator to cache function calls.

    The function will run only once if the inputs are the same.
     In every subsequent run, the results will be pulled from the cache.
      Hence, we don’t have to perform expensive computations all the time.

    The decorator uses a dictionary,
    stores the function args, and returns values.
    When we execute this function, the decorated will check the dictionary for prior results.
     The actual function is called only when there’s no stored value before.

     EX:
        @memoize
        def fibonacci(n):
            if n <= 1:
                return n
            else:
                return fibonacci(n - 1) + fibonacci(n - 2)

    """
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper
