import random
from time import sleep

import pybreaker as pybreaker


breaker = pybreaker.CircuitBreaker(fail_max=3, reset_timeout=5)


@breaker
def fragile_service():
    if random.choice([True, False, False]):
        return "+++OK+++"
    else:
        raise RuntimeError("Service unstable")


if __name__ == "__main__":
    while True:
        try:
            print(fragile_service())
        except pybreaker.CircuitBreakerError:
            print("CIRCUIT BREAKER WORKING - FAILED IMMEDIATELY")
        except Exception:
            print("SERVICE FAILED")
        finally:
            sleep(1)

