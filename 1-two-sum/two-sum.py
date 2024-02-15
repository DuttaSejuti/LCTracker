class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # TC: O(n), SC: O(n)
        new_dict = dict() # value: index
        
        for i in range(len(nums)):
            b = target - nums[i]
            if b in new_dict: #takes O(1)
                return [new_dict.get(b), i]
            new_dict[nums[i]] = i

        # TC: O(n^2), SC: O(1)
        # for i in range(len(nums)):
        #     b = target - nums[i]
        #     if b in nums: #takes O(n)
        #         j = nums.index(b)
        #         if(i == j):
        #             i = i + 1 #same indexed element cannot be the answer
        #         else:
        #             return [i,j]