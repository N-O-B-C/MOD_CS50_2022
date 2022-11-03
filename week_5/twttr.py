def main():
    str_input = input("Enter a string to be shorten: ")
    output = vowel_omittion(str_input)
    print(output)


def vowel_omittion(str_input):
    vowel_exclution = ""
    for letter in str_input:
        if letter.lower() not in  ["a", "i", "e", "o","u"]:
            vowel_exclution += letter
    return(vowel_exclution)

if __name__ == "__main__":
    main()