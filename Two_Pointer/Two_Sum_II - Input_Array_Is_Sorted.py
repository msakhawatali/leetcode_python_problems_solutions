class Solution(object):
    def twoSum(self, numbers, target):
        st = 0
        end = len(numbers)-1
        while st < end :
            if numbers[st]+numbers[end] == target:
                return [st+1, end+1]
            elif numbers[st]+numbers[end] < target:
                st += 1
            else:
                end -= 1