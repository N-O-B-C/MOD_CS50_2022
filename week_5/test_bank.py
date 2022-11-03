from bank import greeting

def main():
    check_for_hello()
    #check_for_h()

def check_for_hello():
    assert greeting("hello") == "$0"
    assert greeting("Hello") == "$0"
    assert greeting("HELLO") == "$0"

def check_for_h():
    assert greeting("hell") == "$20"
    assert greeting("He") == "$20"
    assert greeting("HE") == "$20"

def check_greeting_not_hello():
    assert greeting("goat") == "$100"
    assert greeting("Goat") == "$100"
    assert greeting("GOAT") == "$100"

main()