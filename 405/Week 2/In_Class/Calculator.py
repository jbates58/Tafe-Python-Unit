num1 = 0
num2 = 0
operator = 0
answer = 0

def firstNum():
    global num1
    num1 = int(input("Please enter your FIRST NUMBER: "))

def secondNum():
    global num2
    num2 = int(input("Please enter your SECOND NUMBER: "))

def operation():
    global operator
    while operator != "a" and operator != "s" and operator != "m" and operator != "d":
        operator = str(input("Please select one of the following: a = Add, s = Subtract, m = Multiply, d = Divide: ")).lower()


def equation():
    global answer
    if operator == "a":
        answer = num1 + num2
    elif operator == "s":
        answer = num1 - num2
    elif operator == "m":
        answer = num1 * num2
    else:
        answer = num1 / num2

firstNum()
operation()
secondNum()
equation()
print(answer)