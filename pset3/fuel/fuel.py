while True:
    try:
        x, y = input("Fraction: ").split("/", 2)
        x = int(x)
        y = int(y)
        fuel = (x / y) * 100
    except (ZeroDivisionError, ValueError):
        pass
    else:
        break

if fuel == 100:
    print("F")
elif fuel == 0:
    print("E")
else:
    print(f"{fuel:.0f}%")
