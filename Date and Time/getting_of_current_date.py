from datetime import datetime
import pytz

now = datetime.now()

utcDate = datetime.utcnow()

australiaDate = datetime.now(pytz.timezone('Australia/Sydney'))

londonDate = datetime.now(pytz.timezone('Europe/London'))

print(str(now))
print(utcDate)
print(australiaDate)
print(londonDate)
