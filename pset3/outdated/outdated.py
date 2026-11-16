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
            day = int(day)
            year = int(year)
            print(f"{year}-{month:02d}-{day:02d}")
        elif date.find(",") != -1:
            month_day, year = date.split(", ")
            month, day = month_day.split()
            month = month.title()
            month = months.index(month) + 1
            day = int(day)
            year = int(year)
            print(f"{year}-{month:02d}-{day:02d}")
        break
    except (ValueError, IndexError):
        pass
