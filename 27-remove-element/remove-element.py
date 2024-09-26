# almost similar to the remove duplicates from sorted array algo.
# one pointer to scan and another pointer to point where we going to insert the element that doesn't match the val.
    # does match => move r
    # doesn't match => insert num at pos r to num at pos l, move l, move r
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0 , 0
        while r < len(nums):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
            r += 1
        return l
