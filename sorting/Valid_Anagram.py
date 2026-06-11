class Solution(object):
    def isAnagram(self, s, t):
        s_sorted = "".join(sorted(s))
        t_sorted = "".join(sorted(t))
        if s_sorted == t_sorted:
            return True
        else:
            return False