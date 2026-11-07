def convert(text):
    text = text.replace(":)", "🙂").replace(":(", "🙁")
    print(text)


def main():
    text = input()
    convert(text)


if __name__ == "__main__":
    main()
