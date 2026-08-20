class Solution(object):
    def summaryRanges(self, nums):
        n = len(nums)
        result = []
        i = 0
        while i < n:
            start = nums[i]
            while i+1 < n and nums[i+1] - nums[i] == 1:
                i+=1
            if start != nums[i]:
                result.append(str(start)+"->"+str(nums[i]))
            else:
                result.append(str(start))
            i += 1
        return result