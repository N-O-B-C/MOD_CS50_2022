#seperates white space with triple dots
def sep_dot():
    str_input = input("Enter a sentence: ")
    replacing = str_input.replace(" ", "...")
    return replacing

output = sep_dot()
print(f"Any place you see triple dots it shows there is white space inbetween the two words {output}")
