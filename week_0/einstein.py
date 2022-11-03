#This code prompts a user for input as mass and output the result as equivalent joules


def energy(mass):
    speed_of_light = 300000000
    

    energ = mass * speed_of_light **2 #The formula for energy

    return energ


mass = int(input("Enter your mass valu: "))
result = energy(mass)

print(result, "joules")