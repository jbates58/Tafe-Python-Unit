unsortedNumList = [17, 12, 56, 94, 3, 18, 45, 62, 9, 101, 86, 7]
sortedNumList = []
temp = 0


print(unsortedNumList)

for i in unsortedNumList:
    index = 1
    while unsortedNumList[index] > unsortedNumList[index-1]:
        temp = unsortedNumList[index-1]
        unsortedNumList[index-1] = unsortedNumList[index]
        index = index + 1

print(unsortedNumList)