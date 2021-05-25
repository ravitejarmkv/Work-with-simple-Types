from datetime import datetime, timedelta

now = datetime.today()
yesterday = now - timedelta(days=1)
tomorrow = now + timedelta(days=1)
nextMonth = now.replace(month=now.month+1)
nextYear = now.replace(year=now.year+1)

print(str(now))
print(str(yesterday))
print(str(tomorrow))
print(str(nextMonth))
print(str(nextYear))
