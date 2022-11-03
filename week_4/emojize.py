import emoji

def main():
    emoji_input = input("hello: ")
    output = get_emojized(emoji_input)
    print("hello", end=" ")
    print(output)

def get_emojized(emoji_input):

    return(emoji.emojize(emoji_input))

main()