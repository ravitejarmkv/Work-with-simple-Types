from datetime import datetime

now = datetime.now()
shorStyle = now.strftime("%m/%d/%y %H:%M %p")

customStyle = now.strftime("%Y-%m- %d")

standardStyle = str(now)

strFormat = "Today {0:%d} {0:%B}.".format(datetime.now(), "day", "month")

print(shorStyle)
print(customStyle)
print(standardStyle)
print(strFormat)