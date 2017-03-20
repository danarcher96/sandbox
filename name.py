

def main():
    userName = get_name()
    userNamelen = len(userName)
    steps = input("How steps between each letter printed? ")
    print_name(userName, userNamelen)


def print_name(userName, userNamelen, steps):
    for i in range(0, userNamelen, steps):
        print(userName[i])


def get_name():
    userName = str(input("Enter your name: "))
    return userName


main()