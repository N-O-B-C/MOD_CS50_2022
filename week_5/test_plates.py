"""The lenght of plate should not be more than 6 and not less than 2
   Numbers should not come first within index 0 and 1.
   Zero should not come first before numeric value.
"""
from plates import is_valid

def main():
    check_lenght()
    test_num_first()
    tes_zero_before_num()
    
def check_lenght():
    assert is_valid("et") == True
def test_num_first():
    assert is_valid("vbn12") == True

def tes_zero_before_num():
    assert is_valid("cs05") == True
main()