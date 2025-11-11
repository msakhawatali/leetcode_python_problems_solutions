class Solution(object):
    def mySqrt(self, x):

        st , end = 0 , x
        res = 0
        while st <= end:
            m = st + ((end - st) // 2)
            if m**2 > x:
                end = m - 1
            elif m**2 < x:
                st = m + 1
                res = m
            else:
                return m
        return res