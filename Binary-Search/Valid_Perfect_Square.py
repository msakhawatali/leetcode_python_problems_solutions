class Solution(object):
    def isPerfectSquare(self, num):
        if num < 0:
            return False
        if num == 0 or num ==1:
            return True
        st = 1
        end = num
        while st <= end:
            mid = int(st + (end-st)/2)
            if mid * mid == num:
                return True
            elif mid * mid > num:
                end = mid-1
            else:
                st = mid+1
        return False

        