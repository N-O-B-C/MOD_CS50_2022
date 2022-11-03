"""This code accept input as a string, 
    covert it to time and tell you time of meal"""
import datetime

def main():
    hhmm = input("Enter time: ")
    time = datetime.datetime.strptime(hhmm, "%H:%M").time()

    output = convert(time)
    print(output)

def convert(time):
    if datetime.time(7) <= time <= datetime.time(8):
        meal = "breakfast time"

    elif datetime.time(12) <= time <= datetime.time(13):
        meal = "lunch time"

    elif datetime.time(18) <= time <= datetime.time(19):
        meal = "dinner"
    else:
        meal = " "

    return meal

main()