class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod, right_prod = 1, 1
        result = [1] * len(nums)
        n = len(nums)

        for i in range(1, n):
            left_prod *= nums[i-1]
            result[i] *= left_prod
        
        for i in range(n-2, -1, -1):
            right_prod *= nums[i+1]
            result[i] *= right_prod
        
        return result
