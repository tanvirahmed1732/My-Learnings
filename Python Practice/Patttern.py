def main():
    for i in range(4):
        for j in range(i + 1):
            print("*", end="")
        print()


    for i in range(5):
        print("*", end="")
    print()


    for i in range(3, -1, -1):
        for j in range(i + 1):
            print("*", end="")
        print()


if __name__ == "__main__":
    main()
