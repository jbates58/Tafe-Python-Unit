price = float(1.5)
quantity = 0
discountPercent = int(10)

print("the price of each chocolate bare is: $" + "%.2f" % price)
quantity = int(input("How many chocolate bars do you want to buy? "))
print("You wish to buy ", quantity, "Chocolate Bars")

if quantity >= 20:
        print("The total price is: ", ((quantity * price)*.9))
else:
    print("The total price is: ", (quantity * price))
