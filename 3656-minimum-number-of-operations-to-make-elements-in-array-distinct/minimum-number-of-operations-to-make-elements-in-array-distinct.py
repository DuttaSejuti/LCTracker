class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operation, i = 0, 0
        new_dict = dict()
        
        while len(nums) >= 3 and i < len(nums):
            new_dict[nums[i]] = new_dict.get(nums[i], 0) + 1
            if new_dict[nums[i]] > 1:
                nums = nums[3:]
                operation += 1
                new_dict = dict()
                i = 0
                continue
            i += 1

        if len(nums) < 3:
            new_dict = dict()
            for i in range(len(nums)):
                new_dict[nums[i]] = new_dict.get(nums[i], 0) + 1
                if new_dict[nums[i]] > 1:
                    operation += 1
            return operation
        
        return operation
