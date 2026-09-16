"""A small application that does very little, on purpose."""


def greet(name):
    # Regression introduced on purpose: ignores the name it was given.
    return "Hello, world!"


def main():
    print(greet("world"))


if __name__ == "__main__":
    main()