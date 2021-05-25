str_v = "1-3-2"

list_str = list(str_v)
list_str[2] = "2"
list_str[4] = "3"

str_v = "".join(list_str)

print(str_v)
