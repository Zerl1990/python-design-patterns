import time

from creational.handson.context_factory import load_context

if __name__ == "__main__":
    context1 = load_context("./context.json")
    print(context1)

    context2 = load_context("./context.yaml")
    print(context2)

    print(f"Context 1 is Context 2: {context1 is context2}")

    time.sleep(context1.default_delay)
