#this is a comment

x = input('enter value for x:   ')
y = input('enter value for y:   ')

#create a temporary variable to swap X & Y

temp = x
x = y
y = temp

print('the value of x after swap is:   {}'.format(x))
print('the value of y after swap is:   {}'.format(y))