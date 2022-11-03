"""This could only take three argument on the line of command to draw the inputed value,
 if anything else is typed it prints invalid literal"""
import sys
from pyfiglet import Figlet

def main():
    get_figleted()


def get_figleted():
    figlet = Figlet()
    figlet.getFonts()

    font_input = input("Enter font: ")
    
    try:
        if len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
            figlet.setFont(font = sys.argv[2])
            print(figlet.renderText(font_input))

        else:
            print("invalid literal")

    except:
        print("invalid literal")
        sys.exit(1)

main()