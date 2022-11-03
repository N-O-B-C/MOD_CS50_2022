#This check the prize of coke and only accepts three coin input 25, 10, 5
def main():
    remaining_change = get_coin()
    print(f"Your change is {remaining_change}")


def get_coin():
    amount = 50


    while amount > 0:
        print(f"The amount for coke is {amount}coin")
        coin = int(input("Enter coin: "))
        if coin in [25, 10, 5]:
            amount -= coin
    remaining_change = abs(amount)
    return remaining_change


main()