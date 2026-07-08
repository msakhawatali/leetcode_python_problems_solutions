# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
n = int(input("Enter a number for pattern: "))
for i in range(n):
    for j in range(1, n+1):
        print(j, end=" ")
    print()


# 1 2 3 
# 4 5 6 
# 7 8 9 
n = int(input("Enter a number for pattern: "))
num = 1
for i in range(n):
    for j in range(n):
        print(num, end=" ")
        num += 1
    print()