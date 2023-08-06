import queue
import threading


def queue_processor(queue_size):
    """
    Queue decorators can be used to add functions to a queue and process them in a separate thread or process.

    EX:

     queue_size argument which specifies the maximum number of items that can be queued at once.
      You can use this decorator to add any function to the queue

    @queue_processor(10)
    def process_item(item):
        # code to process an item

    add_to_queue = process_item()
    add_to_queue(item1)
    add_to_queue(item2)
    # etc.

    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            q = queue.Queue(maxsize=queue_size)

            def process_queue():
                while True:
                    item = q.get()
                    func(*item)
                    q.task_done()

            t = threading.Thread(target=process_queue)
            t.daemon = True
            t.start()
            return q.put

        return wrapper

    return decorator
