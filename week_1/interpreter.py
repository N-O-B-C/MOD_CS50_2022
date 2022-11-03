#this code do arethmetic operation.
def main():
  first_num = float(input("Enter your first_num: "))
  operator = input("Enter your operator: ")
  second_num = float(input("Enter tour second_num: "))
  result = maths_calculation(first_num, operator,second_num)
  print(result)

def maths_calculation(first_num, operator, second_num):
    if operator == "*":
        answer = first_num * second_num

    elif operator == "+":
        answer = first_num + second_num

    elif operator == "/":
        answer = first_num / second_num

    elif operator == "-":
        answer = first_num - second_num
        
    else:
        answer = "Your operator is not valid"
    return answer
main()