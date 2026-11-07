choice = (
    input(
        "What is the Answer to the Great Question of Life, the Universe, and Everything? "
    )
    .strip()
    .lower()
)

if (choice == "42") or (choice == "forty-two") or (choice == "forty two"):
    print("Yes")

else:
    print("No")
