class Solution(object):
    def titleToNumber(self, s):
        
        result = 0
        for c in s:
            d = ord(c) - ord("A") + 1
            result= result*26+d
        return result