# import time
#
# import schedule
#
#
# def scheduler(interval):
#     """
#     The Scheduler Decorator is a useful advanced Python decorator that can be
#     used to schedule a function to run at specific times or intervals.
#     This can be particularly useful for tasks like periodically cleaning up temporary files,
#      sending emails at specific times, or updating data from external sources.
#
#     EX: @scheduler(1)
#     """
#
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             schedule.every(interval).minutes.do(func, *args, **kwargs)
#
#             while True:
#                 schedule.run_pending()
#                 time.sleep(1)
#
#         return wrapper
#
#     return decorator
