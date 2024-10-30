class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        peak_index = 0

        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                peak_index = i
                break
        
        return peak_index
