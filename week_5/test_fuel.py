from fuel import fuel_gague

def main():
    check_gage()

def check_gage():
    assert fuel_gague("4/4") == "100%"

main()