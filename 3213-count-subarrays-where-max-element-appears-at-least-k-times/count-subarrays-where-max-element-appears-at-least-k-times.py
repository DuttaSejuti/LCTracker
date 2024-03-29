class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        l, r = 0, 0
        result = 0
        new_dict = dict()
        n = len(nums)

        for r in range(len(nums)):
            if nums[r] == max_num:
                new_dict[max_num] = new_dict.get(max_num, 0) + 1
            while l <= r and new_dict.get(max_num, 0) == k:
                if nums[l] == max_num:
                    new_dict[max_num] -= 1
                result += n - r
                l += 1
        return result

