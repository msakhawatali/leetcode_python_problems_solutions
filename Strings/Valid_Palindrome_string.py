import re
class Solution(object):
    def isPalindrome(self, s):

        s = s.lower()
        a = []
        for i in range(len(s)):
            if s[i].isalnum():
                a.append(s[i])
        for i in range(len(a) // 2):
            if a[i] != a[-1 - i]:
                return False
        return True