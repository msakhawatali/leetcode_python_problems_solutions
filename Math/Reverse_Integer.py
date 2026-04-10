class Solution(object):
    def reverse(self, x):
        if x > 0:
            rev = 0
            while x > 0:
                digit = x % 10
                rev = (rev*10) + digit
                x = x//10
            if rev < -2**31 or rev > 2**31 - 1:
                return 0
            return rev

        else:
            conv_pos = abs(x)
            rev = 0
            while conv_pos > 0:
                digit = conv_pos % 10
                rev = (rev*10) + digit
                conv_pos = conv_pos//10
            if rev < -2**31 or rev > 2**31 - 1:
                return 0
            return -rev