#calculator 

print("My Calculator")
print("choose 1 ADDITION")
print("choose 2 SUBSTRACTION")
print("choose 3  MULTIPLCATION")
print("choose 4  DIVISION")
print("choose 5  EXIT")

def add(num1 ,num2):
    return(num1+num2)

def substract(num1,num2):
    if num1==0:
        return 'try entering value greater than zero'
    return (num1-num2)

def multiply(num1,num2):
    return(num1*num2)

def divide(num1 ,num2):
    if num2==0:
        return "you cannot divide a number by zero"
    return(num1/num2)
while True:
    choice=int(input("Enter your choice: "))
    if choice==5:
        print('Application is now closing , Thanks for using')
        break
    num1=int(input("Enter your first number : "))
    num2=int(input("Enter your second number : "))


    if choice==1:
        print(add(num1,num2))
    elif choice==2:
        print(substract(num1,num2))
    elif choice==3:
        print(multiply(num1,num2))
    elif choice==4:
        print(divide(num1,num2))

    




