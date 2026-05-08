class Solution(object):
    def reverseBits(self, n):
        binary = bin(n)[2:]
        if 32 == len(str(binary)):
            return int(str(binary[::-1]),2)
        else:
            num = 32 - len(str(binary))
            for i in range(num):
                binary = "0" + binary
            return int(str(binary[::-1]),2)