"""
    This code use a module called sys to read through a file,
    and print the lenght of the code.
"""
import sys
def main():
    check_line_argv()

    try:
        file = open(sys.argv[1],"r")
        lines = file.readlines()

    except FileNotFoundError:
        sys.exit("file does not exist.")

    count_line = 0
    for line in lines:
        if check_whiteline_comment(line) == False:
            count_line += 1

    print(count_line)

def check_line_argv():
    if len(sys.argv) < 2:
        sys.exit("Too few command arguement.")

    if len(sys.argv) > 2:
        sys.exit("Too many command argument. ")

    if ".py" not in sys.argv[1]:
        sys.exit("not a python file.")

def check_whiteline_comment(line):
    if line.isspace():
        return True

    if line.lstrip().startswith("#"):
        return True

    return False
main()