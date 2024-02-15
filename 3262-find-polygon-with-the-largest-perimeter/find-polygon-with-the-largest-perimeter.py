class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        addition = 0
        maxPeri = -1
        nums.sort()
        for i in range(len(nums)-1):
            addition += nums[i]
            if addition > nums[i+1]:
                maxPeri = max(maxPeri, addition + nums[i+1])
        return maxPeri