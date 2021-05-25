strValue = "true"
boolValue1 = strValue.lower() == "true"
# boolValue is True

strValue = "false"
boolValue2 = bool(strValue)
# boolValue is True

boolValue3 = bool("")
# boolValue is False

print(str(boolValue1))
print(str(boolValue2))
print(str(boolValue3))
