
import time
from functools import wraps


def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Function Started")
        try:
            return func(*args, **kwargs)
        finally:
            print("Function Completed")
    return wrapper


def time_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        try:
            return func(*args, **kwargs)
        finally:
            end = time.time()
            print("Execution time:", end - start, "seconds")
    return wrapper
