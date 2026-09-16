"""A small application that does very little, on purpose."""


def greet(name):
    return f"Hello, {name}!"


def main():
    print(greet("world"))


if __name__ == "__main__":
    main()