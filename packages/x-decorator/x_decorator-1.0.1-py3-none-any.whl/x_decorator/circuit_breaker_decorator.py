import time
from functools import wraps


class CircuitBreaker:
    """
    Circuit breaker decorators are a pattern used to prevent cascading failures in distributed systems.
     They are used to detect when a remote system is failing or unresponsive and temporarily stop sending requests to it.
     This can prevent other systems from experiencing performance degradation or failure due to the unresponsive system.

     EX:
     @circuit_breaker(failure_threshold=3, recovery_timeout=10)
     def remote_request(url):
        # code to make a request to a remote system

    In this example, the circuit breaker will allow up to three consecutive failures
    before opening the circuit and raising an exception for subsequent requests. Once the circuit is open,
     the decorator will wait for 10 seconds before allowing requests to be sent again.

    Circuit breaker decorators are a useful tool for building resilient and fault-tolerant systems.
    """

    def __init__(self, failure_threshold, recovery_timeout):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.failure_count = 0
        self.last_failure_time = 0

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if self.failure_count > self.failure_threshold:
                elapsed_time = time.time() - self.last_failure_time
                if elapsed_time < self.recovery_timeout:
                    raise Exception("Circuit is open. Retry later.")

            try:
                result = func(*args, **kwargs)
                self.failure_count = 0
                return result
            except:
                self.failure_count += 1
                self.last_failure_time = time.time()
                raise

        return wrapper
