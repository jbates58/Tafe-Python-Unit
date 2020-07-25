# === PROGRAM START === #

# Import Python Simple GUI library and assign it the shorthand 'sg'
import PySimpleGUI as sg
import math


# Define smaller helper functions
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def sqrt(a):
    return math.sqrt(a)


# Define reusable answer function
def getAns(a, b, op):
    ans = 0
    if op == "+":
        ans = add(a, b)
    elif op == "-":
        ans = sub(a, b)
    elif op == "*":
        ans = mul(a, b)
    elif op == "/":
        ans = div(a, b)
    elif op == "SQRT":
        ans = sqrt(a)

    return ans  # Will return 0 if passed an invalid operation


# Setup the answer text field
txtAns = sg.Text(text="0", size=(26, 1), auto_size_text=False, justification="right")
# Setup and position the remaining buttons in rows and columns
guiLayout = [[txtAns],
             [sg.Button("7", size=(5, 2)), sg.Button("8", size=(5, 2)), sg.Button("9", size=(5, 2)), sg.Button("+", size=(5, 2))],
             [sg.Button("4", size=(5, 2)), sg.Button("5", size=(5, 2)), sg.Button("6", size=(5, 2)), sg.Button("-", size=(5, 2))],
             [sg.Button("1", size=(5, 2)), sg.Button("2", size=(5, 2)), sg.Button("3", size=(5, 2)), sg.Button("*", size=(5, 2))],
             [sg.Button("0", size=(19, 2)), sg.Button("/", size=(5, 2))], [sg.Button("=", size=(19, 2)), sg.Button("CLR", size=(5, 2))],
             [sg.Button("SQRT", size=(5, 2))]
             ]

# Open a new GUI window with the previously defined button and text layout
guiWindow = sg.Window(title="Calculator", layout=guiLayout, margins=(30, 50))

# Initialise necessary variables
a = 0  # First number
b = 0  # Second number
op = "+"  # Chosen operation
n = 0;  # Defines which number we're currently editing

# Start window event loop
while True:
    # Wait for new input action
    # NOTE: Program will not continue forward until an event has been called
    event, value = guiWindow.read()
    if event == sg.WIN_CLOSED:  # Window close button
        break

    try:  # Check if the input was a number by casting it with int()
        num = int(event)
        if n == 0:  # Append digit to first number (do not add)
            tmp = str(a) + event
            a = int(tmp)
            txtAns.Update(value=str(a))  # Update display text
        elif n == 1:  # Append digit to second number (do not add)
            tmp = str(b) + event
            b = int(tmp)
            txtAns.Update(value=str(a) + " " + op + " " + str(b))  # Update display text
    except:
        if event == 'CLR':
            # Clear command. Reset all variables and display text
            txtAns.Update(value="0")
            op = '+'
            n = 0
            a = 0
            b = 0
        elif event == '+' or event == '-' or event == '*' or event == '/' or event == "SQRT":
            # Set operation, move to next number and update text
            op = event
            n = 1
            txtAns.Update(value=str(a) + " " + op)
        elif event == '=' and n == 1:
            # Get answer
            try:
                # Get answer and put it into value A for reuse
                a = getAns(a, b, op)
                txtAns.Update(value=str(a))
            except:
                # Tell the user an error occured and reset value A
                a = 0
                txtAns.Update(value="ERR")
            # Reset other values
            b = 0
            n = 0

# === PROGRAM END === #