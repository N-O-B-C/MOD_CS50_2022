#Converts every input to lower case.
def lowercase():
    str_input = input("input a string to be converted to lowercase: ").lower()
    return str_input


output = lowercase()
print(f"The lower case version of your input is {output}")