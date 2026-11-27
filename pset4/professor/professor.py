import random


def main():
    level = get_level()
    correct = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        answer = x + y

        for i in range(3):
            try:
                guess = int(input(f"{x} + {y} = "))
                if guess == answer:
                    correct += 1
                    break
                if i == 2:
                    print("EEE")
                    print(f"{x} + {y} = {answer}")
                    break
                else:
                    print("EEE")
                    continue
            except ValueError:
                print("EEE")
                continue

    print(f"Correct: {correct}")


def get_level():
    level = 0
    while True:
        try:
            level = int(input("Level: "))
            if level < 1 or level > 3:
                continue
            break
        except ValueError:
            pass
    return level


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()
