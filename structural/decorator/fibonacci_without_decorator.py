
CACHE_FB = {0: 0, 1: 1}


def fibonacci(value):
    if value in CACHE_FB:
        return CACHE_FB[value]
    response = fibonacci(value-1) + fibonacci(value-2)
    CACHE_FB[value] = response
    return response


if __name__ == "__main__":
    print(f"Fibonacci 2: {fibonacci(2)}")
    print("-" * 10)
    print(f"Fibonacci 3: {fibonacci(3)}")
    print("-" * 10)
    print(f"Fibonacci 4: {fibonacci(4)}")
    print("-" * 10)
