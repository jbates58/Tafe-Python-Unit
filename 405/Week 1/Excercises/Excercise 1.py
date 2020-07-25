var1 = int(input("Please Enter a Number: "))
var2 = int(input("Please Enter a Number: "))
var3 = int(input("Please Enter a Number: "))
largest = 0

if var1 > var2:
    if var1 > var3:
        largest = var1
elif var2 > var3:
    largest = var2
else:
    largest = var3

print(largest)