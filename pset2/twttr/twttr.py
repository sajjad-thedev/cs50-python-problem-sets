txt = input("Input: ")

for _ in range(len(txt)):
    if txt[_].lower() in ["a", "e", "i", "o", "u"]:
        continue
    else:
        print(txt[_], end="")

print()