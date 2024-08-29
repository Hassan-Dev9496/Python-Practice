import time

def decorator_function(func):
    def wrapper(*args , **kwargs):
        start = time.time()
        result = func(*args , **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end - start} in time")
        return result
    return wrapper

@decorator_function
def example(n):
    time.sleep(n)

example(5)