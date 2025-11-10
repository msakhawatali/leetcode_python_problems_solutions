class Solution(object):
    def addBinary(self, a, b):

        int_a = int(a,2)
        int_b = int(b,2)

        sum_int = int_a + int_b

        return bin(sum_int)[2:]