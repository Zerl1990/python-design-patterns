
CACHE_FB = {0: 0, 1: 1}


def fibonacci(value):
    if value in CACHE_FB:
        return CACHE_FB[value]
    response = fibonacci(value-1) + fibonacci(value-2)
    CACHE_FB[value] = response
    return response


if __name__ == "__main__":
    print(f"Fibonacci 10: {fibonacci(10)}")
