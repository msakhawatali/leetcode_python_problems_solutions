class Solution(object):
    def validPalindrome(self, s):
        st, end = 0, len(s) - 1        
        while st < end:
            if s[st] != s[end]:
                skip_left = s[st + 1 : end + 1]
                skip_right = s[st : end]
                return skip_left == skip_left[::-1] or skip_right == skip_right[::-1]           
            st += 1
            end -= 1            
        return True