# list of valid inputs
valid_input = [5, 10, 25]

# due amount
amount = 50
print("Amount Due:", amount)

# while loop
while True:
    # ask user for input
    # input must be integer
    coin = int(input("Insert coin: "))

    # check if input is valid
    if coin in valid_input:
        # print("Voilà")

        # negative subtraction
        if amount < coin:
            amount = coin - amount
            print("Change Owed:", amount)
        else:
            amount = amount - coin
            if amount == 0:
                print("Change Owed:", amount)
                break
            else:
                print("Amount Due:", amount)
