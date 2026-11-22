months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

while True:
    try:
        date = input("Date: ")
        if date.find("/") != -1:
            month, day, year = date.split("/")
            month = int(month)
            if month > 12:
                continue
            day = int(day)
            if day > 31:
                continue
            year = int(year)
            print(f"{year}-{month:02d}-{day:02d}")
            break
        elif date.find(",") != -1:
            month_day, year = date.split(", ")
            month, day = month_day.split()
            month = month.title()
            month = months.index(month) + 1
            day = int(day)
            if day > 31:
                continue
            year = int(year)
            print(f"{year}-{month:02d}-{day:02d}")
            break
        else:
            continue
    except (ValueError, IndexError):
        pass
