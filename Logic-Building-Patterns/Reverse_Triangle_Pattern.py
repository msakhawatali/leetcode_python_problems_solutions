# 1 
# 2 1 
# 3 2 1 
# 4 3 2 1 

n = int(input("Enter a number: "))

for i in range(n):
    for j in range(i+1, 0, -1):
        print(j, end=" ")
    print()