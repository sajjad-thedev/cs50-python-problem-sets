items = {}

while True:
    try:
        item = input().lower()
        if item in items:
            items[item] += 1
        else:
            items[item] = 1
    except (KeyError, ValueError):
        pass
    except EOFError:
        print()
        break

for item in sorted(items.keys()):
    print(f"{items[item]} {item.upper()}")
