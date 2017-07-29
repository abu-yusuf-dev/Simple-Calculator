
def add(x,y):
   return x+y


def subtract(x,y):
   return x-y


def multiply(x,y):
   return x*y


def divide(x,y):
   return x/y

a=int(input("Please Select a option: \n 1.Add \n 2.Subtraction \n 3.Multiply \n 4.Divide \n"))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if a == '1':
   print(num1,"+",num2,"=",add(num1,num2))

elif a == '2':
    print(num1,"-",num2,"=", subtract(num1,num2))

elif a == '3':
    print(num1,"*",num2,"=", multiply(num1,num2))

elif a == '4':
    print(num1,"/",num2,"=", divide(num1,num2))
else:
    print("Invalid")