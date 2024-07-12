class Solution:
    def search(self, nums: List[int], target: int) -> int:
        new_dict = dict()
        for i in range(len(nums)):
            new_dict[nums[i]] = i
            if nums[i] == target:
                return i
        return -1
       