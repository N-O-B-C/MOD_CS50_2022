#This takes input and calculate the price if only the input is in available_food
available_food = {
                  "Baja Taco": 4.00,
                  "Burrito": 7.50,
                  "Bowl": 8.50,
                  "Nachos": 11.00,
                  "Quesadilla": 8.50,
                  "Super Burrito": 8.50,
                  "Super Quesadilla": 9.50,
                  "Taco":3.50,
                  "Tortilla Salad": 8.00
                  }
def main():
    get_oder()


def get_oder():
    total_amount = 0

    while True:
        try:
            print("Enter control-d to end oder.")
            food_name = input("Enter food name: ").title()

            if food_name in available_food:
                total_amount += available_food[food_name]

            elif food_name == "Control-D":
                break

            print("TOTAL PRICE: ", end="")
            print("{:.2f}".format(total_amount))

        except NameError:
            pass
        
main()