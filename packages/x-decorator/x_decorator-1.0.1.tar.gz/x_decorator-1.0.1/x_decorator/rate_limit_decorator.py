import time
from functools import wraps


def rate_limit(limit, period):
    """
    Throttling
    Rate limiting decorator can be used to limit the number of times
     a function can be called within a certain time period.

     EX:
     @rate_limit(limit=5, period=60)
     def call_dummy_api():
         response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
         return response
    """

    def decorator(func):
        calls = []

        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            calls_in_period = [call for call in calls if now - call <= period]
            if len(calls_in_period) >= limit:
                time_to_wait = period - (now - calls_in_period[0])
                time.sleep(time_to_wait)
            calls.append(now)
            return func(*args, **kwargs)

        return wrapper

    return decorator
