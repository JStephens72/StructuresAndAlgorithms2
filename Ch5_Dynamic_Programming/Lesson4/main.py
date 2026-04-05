def memoize(func):
    cache = {}

    def wrapper(n):
        if n in cache:
            return cache[n]

        result = func(n)
        cache[n] = result
        return result

    return wrapper

@memoize
def fibonacci(n, memo=None):
    if n < 2:
        return n    
    return fibonacci(n - 1) + fibonacci(n - 2)