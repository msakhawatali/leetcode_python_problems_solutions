class Solution(object):
    def reverseWords(self, s):

        n = len(s)
        ans = ""
        s = s[::-1]
        i = 0

        while i < n:
            while i < n and s[i] == " ":
                i += 1

            word = ""
            while i < n and s[i] != " ":
                word += s[i]
                i += 1

            if word:
                if ans:
                    ans += " "
                ans += word[::-1]

        return ans