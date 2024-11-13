# 0, 1, 4, 4, 5, 7
class Solution:
    def findPairsLessThanOrEqualUpper(self, nums: List[int], upper) -> int:
        l, r = 0, len(nums)-1
        count = 0

        while l < r:
            while l < r and r < len(nums) and nums[l] + nums[r] <= upper:
                count += (r-l)
                l += 1
            r -= 1
        return count

    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        pairs_less_than_lower = self.findPairsLessThanOrEqualUpper(nums, lower-1) # this is finding pairs that are less than lower
        pairs_less_than_equal_to_upper = self.findPairsLessThanOrEqualUpper(nums, upper)
        return  pairs_less_than_equal_to_upper - pairs_less_than_lower