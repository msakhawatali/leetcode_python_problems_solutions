n = int(input("Enter a number"))

num = 1

for i in range(n):
    for j in range(i):
        print(" ",end="")

    for j in range(n-i):
        print(i+1, end="")

    print()