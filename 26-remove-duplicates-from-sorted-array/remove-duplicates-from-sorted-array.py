# TC: O(N); SC: O(1)
# two pointers
# 1 pointer to scan through the array - r
# another pointer to put the next unique value - l
# compare r to the prev
    # same value => move R
    # diff value => replace value at l with value at r, move l, move l
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 1, 1
        while r < len(nums):
            if nums[r] == nums[r-1]:
                r += 1
            else:
                nums[l] = nums[r]
                l += 1
                r += 1
        return l

        # shorter version
        # l = 1
        # for r in range(1, len(nums)):
        #     if nums[r] != nums[r-1]:
        #         nums[l] = nums[r]
        #         l += 1
        # return l
