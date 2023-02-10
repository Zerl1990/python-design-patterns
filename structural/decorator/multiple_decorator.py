
def decor1(func):
    def wrap():
        print("************")
        func()
        print("************")
    return wrap


def decor2(func):
    def wrap():
        print("@@@@@@@@@@@@")
        func()
        print("@@@@@@@@@@@@")
    return wrap


@decor1
@decor2
def hello_world():
    print("Hello")


if __name__ == "__main__":
    hello_world()
