from pyfiglet import Figlet
import sys
import random

f = Figlet()

if not len(sys.argv) == 1 and not len(sys.argv) == 3:
    print("Invalid Usage")
    sys.exit(1)


if len(sys.argv) == 1:
    font = random.choice(f.getFonts())
    f.setFont(font=font)
    str = input("Input: ")
    print("Output: ")
    print(f.renderText(str))

else:
    if not sys.argv[1] in ["-f", "--font"]:
        print("Invalid Usage")
        sys.exit(1)
    if not sys.argv[2] in f.getFonts():
        print("Invalid Usage")
        sys.exit(1)
    font = sys.argv[2]
    f.setFont(font=font)
    str = input("Input: ")
    print("Output: ")
    print(f.renderText(str))
