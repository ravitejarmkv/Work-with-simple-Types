import locale

exp = 2.718281828
s1 = str(exp)

s2 = "{0:0.3f}".format(exp)

s3 = "{0:0.2E}".format(exp / 100)

locale.setlocale(locale.LC_ALL, "ru_Ru")

s4 = locale.format_string("%2f", exp * 1000000, grouping=True)

print(s1)
print(s2)
print(s3)
print(s4)
