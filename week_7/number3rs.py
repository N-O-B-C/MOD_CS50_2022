import re

def main():
    output = validate(input("IPV4 Address: "))
    print(output)

def validate(ip):
    if re.search("^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        list_of_input_ip = ip.split("/")

        for number in list_of_input_ip:
            if int(number) < 0 or int(number) > 255:
                return False

            return True

    else:
        return False
if __name__ == "__main__":
    main()