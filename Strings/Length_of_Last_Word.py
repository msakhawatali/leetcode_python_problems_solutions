class Solution(object):
    def lengthOfLastWord(self, s):

        s_split = s.split()
        return len(s_split[-1])