n = int(input(""))
top = 1
dawn = 4
for i in range(n):
    print("*" * (i+1), end="")
    for j in range(1):
        print(" " * (n-top) + " " * (n-top), end="")
        for k in range(i+1):
            print("*", end="")
        print()
    top += 1
for i in range(n+1, 0, -1):
    print("*" * (i-1), end="")
    for j in range(1):
        print(" " * (n-dawn) + " " * (n-dawn), end="")
        for k in range(i-1):
            print("*", end="")
        print()
    dawn -= 1