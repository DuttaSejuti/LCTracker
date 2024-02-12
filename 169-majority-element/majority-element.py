import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        new_dict = dict()
        n_size = len(nums)
        for n in nums:
            new_dict[n] = new_dict.get(n, 0) + 1

        for n in new_dict:
            if new_dict[n] > math.floor(n_size/2):
                return n