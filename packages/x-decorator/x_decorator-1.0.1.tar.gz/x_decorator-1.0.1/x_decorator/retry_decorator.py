import time
from functools import wraps


def retry(max_tries=3, delay_seconds=1):
    """
    When an unexpected event occurs, we might want our code to wait a while, allowing the external system to correct itself and rerun.

    I prefer to implement this retry logic inside a python decorator,
     so that I can annotate any function to apply the retry behavior.

     EX:
        @retry(max_tries=5, delay_seconds=2)
        def call_dummy_api():
            response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
            return response
    """

    def decorator_retry(func):
        @wraps(func)
        def wrapper_retry(*args, **kwargs):
            tries = 0
            while tries < max_tries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    tries += 1
                    if tries == max_tries:
                        raise e
                    time.sleep(delay_seconds)

        return wrapper_retry

    return decorator_retry
