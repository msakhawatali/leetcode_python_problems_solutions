class Solution(object):
    def isPowerOfTwo(self, n):
        power = 0
        while True:
            if 2**power == n:
                return True
            elif 2**power > n:
                return False
            else:
                power += 1