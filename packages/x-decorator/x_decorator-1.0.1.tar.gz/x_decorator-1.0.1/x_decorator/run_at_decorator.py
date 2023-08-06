import datetime
import threading


def run_at(time):
    """
    A Scheduler decorator can be used to schedule the execution of a function
     at a specified time or at a fixed interval.

     EX: @run_at(datetime.datetime(2023, 5, 5, 10, 0, 0))
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            now = datetime.datetime.now()
            delta_t = time - now
            seconds = delta_t.seconds + 1
            timer = threading.Timer(seconds, func, args=args, kwargs=kwargs)
            timer.start()

        return wrapper

    return decorator
