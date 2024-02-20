class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # using math equation for contiguous numbers[0,n]
        # TC: O(n), SC:O(1)
        n = len(nums)
        total_sum = n * (n+1) // 2
        return total_sum - sum(nums)

        #using sorting
        # TC: O(nlogn), SC: O(1)
        # n = len(nums)
        # nums.sort()
        # for i in range(n+1):
        #     if i == n:
        #         return i
        #     if nums[i] != i:
        #         return i

        # using list
        # TC:O(n), SC:O(n)
        # n = len(nums)
        # new_list = [-1] * (n+1)
        # for n in nums:
        #     new_list[n] = n
        # for i in range(len(new_list)):
        #     if new_list[i] == -1:
        #         return i



