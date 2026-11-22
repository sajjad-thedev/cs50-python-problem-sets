import inflect

names = []

while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        break

p = inflect.engine()

print()
print("Adieu, adieu, to", end=" ")
print(p.join(names))
