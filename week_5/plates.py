"""The lenght of plate should not be more than 6 and not less than 2
   Numbers should not come first within index 0 and 1.
   Zero should not come first before numeric value.
"""
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
def is_valid(plate):
    if  len(plate) < 2 or len(plate) > 6:
        return False
    if plate[0:2].isalpha() == False:
        return False
    i = 0
    while i < len(plate):
        if plate[i].isalpha() == False:
            if plate[i] == "0":     #check if 0 comes first befor number
                return False        
            else:
                break
        i += 1
    for item in plate:
        if item in ["!", "?", " ", "."]:
            return False
    return True
if __name__ == "__main__":
    main()