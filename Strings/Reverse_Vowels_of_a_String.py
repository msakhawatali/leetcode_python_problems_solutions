class Solution(object):
    def reverseVowels(self, s):
        s_list = list(s)
        st = 0 
        end = len(s_list) - 1
        vowels = "aeiouAEIOU"
        while st <= end:
            if s_list[st] in vowels and s_list[end] in vowels:
                s_list[st], s_list[end] = s_list[end], s_list[st]
                st += 1
                end -= 1
            elif s_list[st] not in vowels:
                st += 1
            else:
                end -= 1
        return "".join(s_list)
        