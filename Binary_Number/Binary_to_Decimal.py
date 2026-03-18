def binaryToDec(num):
    ans, pow = 0, 1
    while num > 0:
        rem = int(num%10)
        ans += rem*pow
        num = int(num / 10)
        pow *= 2
    return ans

print(binaryToDec(1010))

