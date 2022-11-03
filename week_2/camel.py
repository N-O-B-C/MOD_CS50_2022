#This change input from camelcase to snakecase
def main():
    name = input("camelCase: ")
    print(f"snake_case: {change_case(name)}")

def change_case(name):
    res = [name[0].lower()]
    for c in name[1:]:
        if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            res.append('_')
            res.append(c.lower())
        else:
            res.append(c)
     
    return "".join(res)
     

main()