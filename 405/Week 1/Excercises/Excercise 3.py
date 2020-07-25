
textString = str(input("Please enter a string of text.")).lower()
print("your string of text is: " + textString)



#  Print out the quantity of SPACES in the text string
spaces = 0
for s in textString:
    if s == " ":
        spaces = spaces + 1
print("The quantity of spaces in your string is: ", spaces)

#  print out the quantity of NUMBERS in the text string
numbers = 0
for n in textString:
    if n == "0" or n == "1" or n == "2" or n == "3" or n == "4" or n == "5" or n == "6" or n == "7" or n == "8" or n == "9":
        numbers = numbers + 1
print("The quantity of NUMBERS in your string is: ", numbers)

#  print out the quantity of VOWELS in the text string
vowels = 0
for v in textString:
    if v == "a" or v == "e" or v == "i" or v == "o" or v == "u":
        vowels = vowels + 1
print("The quantity of VOWELS in your string is: ", vowels)

#  print out the quantity of CONSONANTS in the text string
consanants = 0
for c in textString:
    if c == "b" or c == "c" or c == "d" or c == "f" or c == "g" or c == "h" or c == "j" or c == "k" or c == "l" or c == "m" or c == "n" or c == "p" or c == "q" or c == "r" or c == "s" or c == "t" or c == "v" or c == "w" or c == "x" or c == "y" or c == "z":
        consanants = consanants + 1
print("The quantity of CONSANANTS in your string is: ", consanants)
