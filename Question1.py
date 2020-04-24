a = float(input("Enter first number :"))
b = float(input("Enter second number :"))
x = input("Choose Operator +, - , / , * :")
if x == '+':
    print("Answer :", a+b)
if x == '-':
    if a>b:
        print("Answer :", a-b)
    else:
        print("Answer :", b-a)
elif x == '/':
    print("Answer :", a/b)
elif x == '*':
    print("Answer :", a*b)
else:
    print('Invalid')
    