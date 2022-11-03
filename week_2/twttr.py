#This code omit's all vowel in a giving string
def main():
    
    vowel_omittion()
    

def vowel_omittion():
    str_input =input("Enter a string: ").lower()
    for letter in str_input:
        if letter in  ["a", "i", "e", "o","u"]:
            continue
        print(letter,end='')


main()