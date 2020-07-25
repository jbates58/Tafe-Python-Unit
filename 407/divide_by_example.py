def div42by(divideby):
    try:
        return 42 / divideby
    except ZeroDivisionError:
        print('Error, you tried to divide by Zero')

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))
