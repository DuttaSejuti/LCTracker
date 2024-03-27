class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0
        l, r = 0, 0
        multi = 1

        for r in range(len(nums)):
            multi *= nums[r]
            while l < r and multi >= k:
                multi = multi / nums[l]
                l += 1

            if multi < k:
                count += (r-l+1)

        return count

    # TC: O(n^2), SC:O(1) => TLE
    # def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
    #     count = 0

    #     for i in range(len(nums)):
    #         multi = nums[i]
    #         if multi < k:
    #             count += 1
    #         for j in range(i+1,len(nums)):
    #             multi *= nums[j]
    #             if multi < k:
    #                 count += 1
    #             else:
    #                 break
    #     return count
