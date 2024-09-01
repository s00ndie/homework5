answer = 'y'
while answer == 'y' or answer== 'yes':
    int1 = int(input('Enter first number:'))
    int2 = int(input('Enter second number:'))
    oper = input('Choose operation \'+,-,/,*\':')
    if oper == '+':
        print(int1 + int2)
    elif oper == '-':
        print(int1 - int2)
    elif oper == '/' and int2 != 0:
        print(int1 / int2)
    elif oper == '*':
        print(int1*int2)
    else:
        print("It's impossible")
    answer = input('Enter \'yes\' if you want continue:')