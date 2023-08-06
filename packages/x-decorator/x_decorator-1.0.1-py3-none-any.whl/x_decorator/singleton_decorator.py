from functools import wraps


def singleton(cls):
    """
    Class-based singleton enforcement
    The singleton decorator can be used to ensure that only one instance of a class is ever created.

    EX:
    @singleton
    class MySingletonClass:
        # code for MySingletonClass
    """
    instances = {}

    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance
