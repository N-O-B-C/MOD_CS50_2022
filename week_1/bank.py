#This code shows the amount to pay depending on your greeting.
def main():
    greet = input("Greet: ")
    prise = greeting(greet)

    print(f"Your prise is {prise}")

def greeting(greet):
    if greet == "hello".lower():
        prise = "$0"

    elif greet[0] == "h".lower():
        prise = "$20"


    else:
        prise = "$100"

    return prise

main()