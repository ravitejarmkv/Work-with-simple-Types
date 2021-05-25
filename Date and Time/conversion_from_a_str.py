from datetime import datetime
from dateutil import parser

# the first method
stringDate = "2018-01-31 11:47"
victoryDate1 = datetime.strptime(stringDate, "%Y-%m-%d %I:%M")

# Second method
victoryDate2 = parser.parse(stringDate)

print(victoryDate1)
print(victoryDate2)

