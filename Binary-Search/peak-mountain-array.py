class Solution(object):
    def peakIndexInMountainArray(self, arr):
        st = 0
        end = len(arr)-1
        peak_dix = 0
        while st <= end:
            mid = int(st + (end-st)/2)
            if arr[mid] > arr[peak_dix]:
                peak_idx = mid
            if arr[mid] < arr[mid+1]:
                st = mid + 1
            else:
                end = mid - 1
        return peak_idx