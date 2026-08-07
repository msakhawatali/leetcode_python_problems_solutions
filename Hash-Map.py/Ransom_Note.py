class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        hash_map = {}
        for i in ransomNote:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1

        for  i in magazine:
            if i in hash_map:
                hash_map[i] -= 1
                if hash_map[i] == 0:
                    del hash_map[i]

        if not hash_map:
            return True
        else:
            return False