"""
    This code accept date of birth, year month and day  as a string, 
    and find the minutes spent within the years.
"""
from datetime import date
import re
import sys
import inflect

p = inflect.engine()

def main():
    birth_date = input("Date of birth: ")
    try:
        year, month, day = check_birth_date(birth_date)
    except:
        sys.exit("invalid date")

    date_of_birth = date(int(year) , int(month), int(day))

    date_of_today = date.today()
    diff = date_of_today - date_of_birth
    total_minutes = diff.days * 24 *60
    output = p.number_to_words(total_minutes)

    print(output.capitalize() + " minutes")
def check_birth_date(birth_day):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birth_day):
        year, month, day = birth_day.split("-")
        return year, month, day

main()