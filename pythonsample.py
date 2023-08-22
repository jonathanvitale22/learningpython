def main():
    name = input("Who the heck? ")
    hello(name.strip().title())


def hello(to="world"):
    print("hello,", to)


main()