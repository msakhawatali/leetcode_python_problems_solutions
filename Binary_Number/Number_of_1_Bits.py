class Solution(object):
    def hammingWeight(self, n):
        count = 0
        binary = str(bin(n)[2:])
        for i in range(len(binary)):
            if binary[i] == '1':
                count += 1
        return count