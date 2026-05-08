s = "babad"
start = 0
end = len(s)
rever_s = reversed(s[start:end])
while s != rever_s:
    start += 1
    end -= 1
print(rever_s) 