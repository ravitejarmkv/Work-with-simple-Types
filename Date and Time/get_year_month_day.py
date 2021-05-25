from datetime import datetime
now = datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second
dayOfWeek = now.isoweekday()

print("Current time: {}.".format(now))
print("Current year: {}.".format(year))
print("Current month: {}.".format(month))
print("Current day: {}.".format(day))
print("Current hour: {}.".format(hour))
print("Current minute: {}.".format(minute))
print("Current second: {}.".format(second))
print("Current day of week: {}.".format(dayOfWeek))