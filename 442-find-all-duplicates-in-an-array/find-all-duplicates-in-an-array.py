# IDEA
# we are using index to traverse the array
# we are making the visited number negative, to sustain it's own value, and marking that we have visited the index
# suppose [4,3,1,1], n=4, we obviously can have 0,1,2,3 index value as the array can only contain values within [1-n]
# we are doing [n-1] to access 0-indexed array value.
# n = 4, nums[4-1] = 1 > 0 [4,3,1,-1]
# n = 3, nums[3-1] = 1 > 0 [4,3,-1,-1]
# n = 1, nums[1-1] = 4 > 0 [-4,3,-1,-1]
# n = 1, nums[1-1] = 4 < 0 res = [1]
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []

        for n in nums:
            n = abs(n)
            if nums[n-1] < 0:
                res.append(n)
            nums[n-1] = -nums[n-1]
        return res
        