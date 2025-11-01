haystack = "sadbutsad"
needle = "sad"
len_needle = len(needle)
if haystack[:len_needle] == needle:
    print(0)
else:
    print(-1)
