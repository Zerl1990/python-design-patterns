import datetime
from retrying import retry

START_TIME = datetime.datetime.now()

DEF_WAIT_TIME_MS = 2000


def waiting_service(*args, **kwargs):
    print(f"Customer service is not replying back, retrying in {DEF_WAIT_TIME_MS} ms")
    return DEF_WAIT_TIME_MS


@retry(wait_func=waiting_service)
def get_customer_info(customer_id):
    print(f"Get customer information: {customer_id}")
    delta = datetime.datetime.now() - START_TIME
    if delta.seconds < 10:
        raise RuntimeError("Service is not responding back")
    else:
        return {"name": "qa minds"}


if __name__ == "__main__":
    get_customer_info("EDS1231DDS")

