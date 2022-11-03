def main():
    fuel = input("Enter a fraction: ")
    print(fuel_gague(fuel))


def fuel_gague(fuel):
    while True:
        try:
            numerator, denominator = fuel.split("/")
            new_numerator = int(numerator)
            new_denominator = int(denominator)
            
            operation = new_numerator / new_denominator

            if operation <= 1:
                break
            else:
                fuel = input("Enter a fraction: ")

        except (ValueError, ZeroDivisionError):
            fuel = input("Enter a fraction: ")

    output = int(operation * 100)

    if output < 1:
        return "E"

    elif output >= 99:
        return "F"


    else:
        return f"{output}%"

if __name__ == "__main__":
    main()