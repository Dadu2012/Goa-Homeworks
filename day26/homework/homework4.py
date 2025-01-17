def calculator(num1, num2, operator):
    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        if num2 != 0: 
            print(num1 / num2)
        else:
            print("0 ზე გაყოფა არ შეიძლება")
    else:
        print("არასწორია ოპერატორი")
        calculator(1293, 209, "+")