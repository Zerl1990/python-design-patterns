import functools


def memoization(fn):
    cache = dict()

    @functools.wraps(fn)
    def memoizer(*args):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]
    return memoizer


@memoization
def fibonacci(value):
    if value in (0, 1):
        return value
    else:
        return fibonacci(value-1) + fibonacci(value-2)


if __name__ == "__main__":
    print(f"Fibonacci 10: {fibonacci(10)}")


