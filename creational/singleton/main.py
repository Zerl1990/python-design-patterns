from creational.singleton.context import Context

if __name__ == "__main__":
    context_1 = Context()
    context_1.name = "My application"

    context_2 = Context()
    print(context_2.name)

    print(f"Context 1 is Context 2: {context_1 is context_2}")
    print(f"Context 1 memory {id(context_1)}")
    print(f"Context 2 memory {id(context_2)}")

