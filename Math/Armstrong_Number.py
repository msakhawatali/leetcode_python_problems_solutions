def isArmstorng(n):
    copyN = n
    sumofCubes = 0
    while n != 0:
        dig = n % 10    
        sumofCubes += (dig * dig * dig) 
        n = int(n / 10)
    return sumofCubes == copyN


    

n = 153
if isArmstorng(n):
    print("is an armstorng number")
else:
    print("not an armstorng number")