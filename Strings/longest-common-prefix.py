class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()
        common_prefix = ''
        n = 0
        for i in strs[0]:
            if i == strs[len(strs)-1][n]:
                common_prefix += i
                n += 1
                continue
            else:
                break
        return common_prefix
    