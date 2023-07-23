import time
from functools import wraps


def timeit(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Finished {func.__name__} in {end - start}")
    return wrap


def timeit_async(func):
    @wraps(func)
    async def wrap(*args, **kwargs):
        start = time.time()
        await func(*args, **kwargs)
        end = time.time()
        print(f"Finished {func.__name__} in {end - start}")
    return wrap
