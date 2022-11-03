#this code output yes if input is 42 and No if other wise
def main():
    num = input("Input your value: ")
    output = get_num(num)

    print(output)

def get_num(num):
    if num == "42":
        answer = "Yes"

    elif num == "forty two":
        answer = "Yes"

    elif num == "forty-two":
        answer = "Yes"

    else:
        answer = "No"

    return answer

main()