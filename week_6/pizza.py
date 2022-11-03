"""This code read through a csv file and print the data in the file 
    in grid tabular form
"""
import sys
import csv
from tabulate import tabulate


def main():
    check_lenght_argv()

    table = []

    try:
        with open(sys.argv[1], "r") as file:
           reader = csv.reader(file)

           for row in reader:
            table.append(row)

        print(tabulate(table[1:],headers = table[0], tablefmt="grid")) 

    except FileNotFoundError:
        sys.exit("csv file does not exist.")
        
def check_lenght_argv():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguement")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguement.")

    if ".csv" not in sys.argv[1]:
        sys.exit("Not a csv file.")

main()