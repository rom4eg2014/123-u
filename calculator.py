while True:
    calc1 = input("Enter the first number:")
    calc2 = input("Enter the second number:")
    calc3 = input("What do you want to do (+,-,*,/):")

    if calc3 == "+":
        answer1 = (int(calc1) + int(calc2))
        print(str(answer1))
    
    if calc3 == "-":
        answer1 = (int(calc1) - int(calc2))
        print(str(answer1))

    if calc3 == "*":
        answer1 = (int(calc1) * int(calc2))
        print(str(answer1))

    if calc3 == "/":
        answer1 = (int(calc1) / int(calc2))
        print(str(answer1))
