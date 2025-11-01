class Solution(object):
    def checkInclusion(self, s1, s2):

        def isFreqSame(freq1, freq2):
            for i in range(26):
                if freq1[i] != freq2[i]:
                    return False
            return True

        def checkInclusion(s1, s2):
            if len(s1) > len(s2):
                return False

        freq1 = [0] * 26
        for c in s1:
            freq1[ord(c) - ord('a')] += 1

        freq2 = [0] * 26
        for i in range(len(s2)):
            freq2[ord(s2[i]) - ord('a')] += 1

            if i >= len(s1):
                freq2[ord(s2[i - len(s1)]) - ord('a')] -= 1

            if isFreqSame(freq1, freq2):
                return True

        return False