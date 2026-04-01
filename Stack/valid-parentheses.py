s = "}([]{"
my_dict = {}
for i in s:
    if i == '(':
        my_dict[')'] = i
    if i in my_dict:
        del my_dict[i]
    if i == '{':
        my_dict['}'] = i
    if i in my_dict:
        del my_dict[i]
    if i == '[':
        my_dict[']'] = i
    if i in my_dict:
        del my_dict[i]
if my_dict == {}:
    print(True)
else:
    print(False)