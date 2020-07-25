# Ask the user for their address

streetNumber = input("Please put in your street number: ")
streetName = input("Please input your street name: ")
suburb = input("Please input your suburb ")
state = input("Please input your state: ")
postCode = input ("Please input your postcode :")

#Print out the address formated as per tast requirements
print(streetNumber + " " + streetName)
print(suburb)
print(state + '\t' + postCode)