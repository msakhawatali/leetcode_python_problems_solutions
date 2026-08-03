class Solution(object):
    def firstUniqChar(self, s):
        unordered_map = {}
        for char in s:
            unordered_map[char] = unordered_map.get(char, 0) + 1
            
        for i in range(len(s)):
            if unordered_map[s[i]] == 1:
                return i 
                
        return -1