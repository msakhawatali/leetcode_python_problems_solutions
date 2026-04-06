class Solution(object):
    def reverseWords(self, s):
        w = s.split()
        w.reverse()
        return " ".join(w)