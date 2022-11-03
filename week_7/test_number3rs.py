from number3rs import validate

def main():
    check_lenght()


def check_lenght():
    assert validate("25.55.24.45")  == True

main()