class Solution(object):
    def subsets(self, nums):

        result = []
        def backtracking(index, current_subset):
            if index == len(nums):
                result.append(list(current_subset))
                return
            current_subset.append((nums[index]))
            backtracking(index+1, current_subset)

            current_subset.pop()

            backtracking(index+1, current_subset)

        backtracking(0,[])
        return result
