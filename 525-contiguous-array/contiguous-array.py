class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_len = 0
        ps = 0
        prefix_sum_index= dict()
        prefix_sum_index[0] = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                ps += -1
            else:
                ps += nums[i]

            known_variable = (ps - 0) 
            index = prefix_sum_index.get(known_variable)
            if index is not None:
                max_len = max(max_len, i-index) 

            prefix_sum_index[ps] = prefix_sum_index.get(ps, i)

            # for j in range(0, i):
            #     condition = (prefix_sum[j] == known_variable)
            #     # condition = (prefix_sum[i] - prefix_sum[j] == k)
            #     count += condition
        return max_len