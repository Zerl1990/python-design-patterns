import functools
import os


def admin(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        admin_access = eval(os.environ.get("ADMIN", "False"))
        if admin_access:
            return func(*args, **kwargs)
        else:
            raise AttributeError(f"{func} REQUIRES ADMIN ACCESS!!!")
    return wrapper
