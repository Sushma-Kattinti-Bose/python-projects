def calulator(op1, op2, op):
    if op == '+':
        return op1 + op2
    elif op == '-':
        return op1 - op2
    elif op == '*':
        return op1 * op2
    elif op == '/':
        return op1 / op2
cont = 'y'
while cont != 'n':
    print("Enter the first number")
    num1 = int(input())
    print("Enter the Second number")
    num2 = int(input())
    print("Enter the Operation")
    op = input()
    if op == '/' and num2 == 0:
        print("Cannot divide by zero")
        continue
    else:
        print(calulator(num1, num2, op))
    print("Do you want to continue(y/n)?")
    cont = input()