class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        new_dict = dict()
        l, r = 0, 0
        max_len = 0 

        for r in range(len(nums)):
            num = nums[r]
            new_dict[num] = new_dict.get(num, 0) + 1
            while new_dict[num] > k:
                left_num = nums[l]
                new_dict[left_num] -= 1
                l += 1
            max_len = max(max_len, r-l+1)

        return max_len