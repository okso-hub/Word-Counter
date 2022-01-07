from os import system, name


clear = lambda: system("clear") if name == "posix" else system("cls")


def main():
    text = str(input("Enter text:\n"))

    split_text = text.split(" ")

    print(f"\nThere are {len(split_text)} words in this text.")


if __name__ == "__main__":
    clear()
    main()
