def main():
    greet = input("Greet: ")
    prise = greeting(greet)

    print(f"Your prise is {prise}")

def greeting(greet):
    if greet.lower() == "hello":
        prise = "$0"

    elif greet.lower()[0] == "h":
        prise = "$20"


    else:
        prise = "$100"

    return prise

if __name__ == "__main__":
    main()