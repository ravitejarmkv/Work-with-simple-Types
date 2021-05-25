from datetime import datetime, timedelta
now = datetime.now()
yesterday = now - timedelta(days=1)

areEqual = now == yesterday
# areEqual is False

areLater = now > yesterday
# areLater is True

areEarlier = now < yesterday
# areEarlier is False

print(str(now))
print(str(yesterday))
print(str(areEqual))
print(str(areLater))
print(str(areEarlier))

