amount = 50
change_owed = 0

while amount > 0:
    print(f"Amount Due: {amount}")
    coin = int(input("Insert Coin: "))

    if coin == 25 or coin == 10 or coin == 5:
        amount -= coin


if amount < 0:
    change_owed = amount * (-1)

print(f"Change Owed: {change_owed}")
