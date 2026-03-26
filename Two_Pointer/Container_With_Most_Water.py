class Solution(object):
    def maxArea(self, height):
        st, end = 0, len(height) - 1
        max_area = 0  
        while st < end:
            h = min(height[st], height[end])
            w = end - st            
            max_area = max(max_area, h * w)            
            if height[st] < height[end]:
                st += 1
            else:
                end -= 1                
        return max_area