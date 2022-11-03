#shows a happy or an agree mog.
import emoji

def main():
    mog = convert()

    if mog == ":)":
        output = ("A happy face","\U0001F642") # prints a happy face

    elif mog == ":(":
        output = ("A sad face","\U0001F612") # prints a sad face

    else:
        output = mog

    print(output)

def convert():
    str_input = input("Input something to impliment: ")
    return str_input

main()