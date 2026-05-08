class Solution(object):
    def strStr(self, haystack, needle):
        len_needle = len(needle)
        for i in range(len(haystack) - len_needle + 1):
            if haystack[i:i+len_needle] == needle:
                return i
        return -1