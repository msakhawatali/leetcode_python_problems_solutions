unsorted_list = [4,1,5,2,3]
n = len(unsorted_list)

for i in range(n-1):
    for j in range(n-i-1):
        if unsorted_list[j]> unsorted_list[j+1]:
            unsorted_list[j],unsorted_list[j+1]=unsorted_list[j+1],unsorted_list[j]
print(unsorted_list)