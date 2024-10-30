# Linear Solution O(n) TC
# class Solution:
#     def peakIndexInMountainArray(self, arr: List[int]) -> int:
#         peak_index = 0

#         for i in range(len(arr)-1):
#             if arr[i] > arr[i+1]:
#                 peak_index = i
#                 break
        
#         return peak_index

# Binary Search O(nlogn)
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr)-1

        while l < r:
            m = (l+r) // 2
            if arr[m] < arr[m+1]: # we are still in the increasing phase, peak idx is in right
                l = m+1
            else:
                r = m # we are in decreasing phase, peak is either mid or some idx smaller than mid, go left
        return l