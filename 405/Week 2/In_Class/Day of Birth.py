from _datetime import datetime

#dobString = str(input("please enter your D.O.B as follows: YYYY,MM,DD"))
dobString = '1989, 05, 29'

date = datetime.strptime(dobString, "%Y, %m, %d")
print(date.weekday())










