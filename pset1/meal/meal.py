def main():
    time = input("What time is it? ").strip()

    hours = convert(time)

    if hours >= 7 and hours <= 8:
        print("breakfast time")

    elif hours >= 12 and hours <= 13:
        print("lunch time")

    elif hours >= 18 and hours <= 19:
        print("lunch time")


def convert(time):
    hrs, mins = time.split(":")
    hrs = float(hrs)
    mins = float(mins)

    result = hrs + (mins / 60)
    return result


if __name__ == "__main__":
    main()
