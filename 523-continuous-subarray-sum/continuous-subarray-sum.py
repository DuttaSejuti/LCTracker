class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        temp = 0
        new_dict = {0:-1}
        for j in range(len(nums)):
            temp += nums[j]
            rem = temp % k
            if rem not in new_dict:
                new_dict[rem] = j
            else:
                if j - new_dict[rem] >= 2:
                    return True
        return False
