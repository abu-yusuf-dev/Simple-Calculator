calculator = True

while calculator:
    print("1 = Addition")
    print("2 = Subtraction")
    print("3 = Multiplication")
    print("4 = Division")
    print("5 = Exit program")
    a = int(input("Enter options : \n"))
    if a == 1:
        print("Addition")
        first = int(input("Enter first number :\n"))
        second = int(input("Enter second number :\n"))
        result = first + second
        print(first ,'+' ,second ,'=' , result)
    elif a == 2:
        print("Subtraction")
        first = int(input("Enter first number :\n"))
        second = int(input("Enter second number :\n"))
        result = first - second
        print(first ,"-" ,second ,"=" , result)
    elif a== 3:
        print("Multiplication")
        first = int(input("Enter first number :\n"))
        secund = int(input("Enter second number :\n"))
        result = first * secund
        print(first ,"*" ,secund ,"=" , result)
    elif a == 4:
        print("Division")
        first = int(input("Enter first number :\n"))
        secund = int(input("Enter second number :\n"))
        result = first / secund
        print(first ,"/" ,secund ,"=" , result)
    elif a == 5:
        print("Quit!")
        calculator = False