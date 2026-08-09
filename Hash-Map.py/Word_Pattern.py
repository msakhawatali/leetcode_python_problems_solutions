class Solution(object):
    def wordPattern(self, pattern, s):
        s_split = s.split(" ")
        if len(pattern) != len(s_split):
            return False
        map_pattern_to_s_split = {}
        map_s_split_to_pattern = {}
        
        for c1, c2 in zip(pattern, s_split):

            if c1 in map_pattern_to_s_split and map_pattern_to_s_split[c1] != c2:
                return False

            if c2 in map_s_split_to_pattern and map_s_split_to_pattern[c2] != c1:
                return False

            map_pattern_to_s_split[c1] = c2
            map_s_split_to_pattern[c2] = c1
            
        return True
        