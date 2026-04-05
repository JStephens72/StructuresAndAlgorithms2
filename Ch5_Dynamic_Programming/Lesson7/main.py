def tabulate(max_n):
    print(f"[tabulate] Creating decorator for max_n = {max_n}")

    def decorator(func):
        print(f"[decorator] Received function: {func.__name__}")

        # Build the table bottom-up
        table = [None] * (max_n + 1)
        print(f"[decorator] Allocated table of size {max_n + 1}")

        for n in range(max_n + 1):
            print(f"[decorator] Computing table[{n}] by calling {func.__name__}({n}, table)")
            table[n] = func(n, table)
            print(f"[decorator] table[{n}] = {table[n]}")

        # This wrapper replaces your original function
        def wrapper(n):
            print(f"[wrapper] Called with n = {n}")
            print(f"[wrapper] Returning table[{n}] = {table[n]}")
            return table[n]

        print(f"[decorator] Finished building table. Returning wrapper.")
        return wrapper

    return decorator

@tabulate(100)
def fibonacci(n, table):
    print(f"    [fibonacci] Called with n = {n}")
    if n < 2:
        print(f"    [fibonacci] Base case: return {n}")
        return n
    result = table[n-1] + table[n-2]
    print(f"    [fibonacci] Computed table[{n-1}] + table[{n-2}] = {result}")
    return result
