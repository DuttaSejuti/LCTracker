# 1,1,2,2,3,7
# 1,2,3,4,5,7
# m = 1+1+2+2

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        moves = 0
        for i in range(1, len(nums)):
            # nums[i-1] > nums[i] can be, because we are doing nums[i] = nums[i-1] + 1
            # 1,1,2,2 => 1,2,2,2 => 1,2,3,2 => nums[i-1] > nums[i] => 3 > 2
            if nums[i-1] >= nums[i]:
                moves += (nums[i-1] - nums[i] + 1)
                nums[i] = nums[i-1] + 1
        return moves

        