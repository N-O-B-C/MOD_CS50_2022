#This code joins multiple string in a list as a sentence.
import inflect

p = inflect.engine()

names = []

while True:
    try:
        name = input("Name: ")
        names.append(name)
        if name == "break":
            break

    except ValueError:
        print()
        break
names.pop()
output = p.join(names)
print(f"Adieu, adieu to {output}")