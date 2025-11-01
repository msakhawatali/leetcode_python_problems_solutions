arr = [4,1,5,2,3]
n = len(arr)

for i in range(n-1):
    smallestIds = i
    for j in range(i+1, n):
        if arr[j] < arr[smallestIds]:
            smallestIds = j
    arr[i], arr[smallestIds] = arr[smallestIds], arr[i]
print(arr)