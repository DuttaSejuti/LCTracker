class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # TC:O(n), SC:O(1)
        max_num = max(nums)
        l, r = 0, 0
        result = 0
        count = 0
        n = len(nums)

        for r in range(len(nums)):
            if nums[r] == max_num:
                count += 1
            while l <= r and count == k:
                if nums[l] == max_num:
                    count -= 1

                # this makes sure that the window itself a valid subarray
                # plus all the subarrays with the rest of the right elemets are also valid
                result += n - r
                l += 1
        return result

