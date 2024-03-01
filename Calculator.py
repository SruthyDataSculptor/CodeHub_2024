
def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2

while True:
    print('*'*100)
    print("Calculator")
    print('*'*100)
    print('1.Add')
    print("2.Subtract")
    print("3.Multiplication")
    print("4.Division")
    print("5.Quit")
    option=input("Select your option : 1,2,3,4,5: ")

    if option=='5':
        print("Exiting program: ")
        break
    num1 = float(input("Enter your 1st number: "))
    num2 = float(input("Enter your 2nd number: "))
    if option=='1':
        print("Result is: ",add(num1,num2))
    elif option == '2':
        print("Result is: ", sub(num1, num2))
    elif option == '3':
        print("Result is: ", mul(num1, num2))
    elif option == '4':
        print("Result is: ", div(num1, num2))
    else:
        print("Invalid option")
