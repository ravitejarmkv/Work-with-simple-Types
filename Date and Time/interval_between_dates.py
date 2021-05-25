from datetime import datetime

reqDate = datetime(year= 1994, month= 5, day= 10)
currentDate = datetime.now()
delta = currentDate - reqDate

days = delta.days
minutes = delta.seconds//60
seconds = delta.seconds

print(reqDate)
print(currentDate)
print(days)
print(minutes)
print(seconds)
