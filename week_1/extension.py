#This code interpretes file extention
import mimetypes
import os

os.listdir()
def main():
    file_name = input("Enter name of a file: ")
    output = file_extension(file_name)
    mytype = mimetypes.guess_type(output)
    print(mytype)

def file_extension(fiel_name):
    return fiel_name

main()