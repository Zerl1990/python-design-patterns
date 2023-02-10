import functools


def memoization(fn):
    cache = dict()

    def wrap(*args):
        if args not in cache:
            print(f"Cache miss: {args}")
            cache[args] = fn(*args)
        else:
            print(f"Cache hit: {args}")
        return cache[args]
    return wrap


@memoization
def fibonacci(value):
    if value in (0, 1):
        return value
    else:
        return fibonacci(value-1) + fibonacci(value-2)


if __name__ == "__main__":
    print(f"Fibonacci 2: {fibonacci(2)}")
    print("-" * 10)
    print(f"Fibonacci 3: {fibonacci(3)}")
    print("-" * 10)
    print(f"Fibonacci 4: {fibonacci(4)}")
    print("-" * 10)


