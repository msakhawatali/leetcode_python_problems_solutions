digit = 12345
count = 0
while 0 < digit:
    list_dig = digit%10
    count += list_dig
    digit = int(digit/10)
print(count)