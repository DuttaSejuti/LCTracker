# TC: O(n^2), SC: O(1) => TLE
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] == nums[j]:
#                     return True
#         return False

# TC: O(n), SC:O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new_dict = dict()
        for num in nums:
            new_dict[num] = new_dict.get(num, 0) + 1
            if new_dict[num] > 1:
                return True
        return False

