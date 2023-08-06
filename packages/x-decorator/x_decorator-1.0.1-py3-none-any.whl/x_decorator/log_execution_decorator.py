import logging
from functools import wraps

logging.basicConfig(level=logging.INFO)


def log_execution(func):
    """
    If you follow software design principles, you’d appreciate the single responsibility principle.
    This essentially means each function will have its one and only one responsibility.

    EX:
    @log_execution
    def extract_data(source):
        # extract data from source
        data = ...

        return data
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Executing {func.__name__}")
        result = func(*args, **kwargs)
        logging.info(f"Finished executing {func.__name__}")
        return result

    return wrapper
