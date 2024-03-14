class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # TC: O(n), SC: O(n)
        freq = dict() # prefix_sum: # of occurances of this prefix_sum
        freq[0] = 1 # to resolve the case where we get prefix_sum = 0 in future
        result = 0
        prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]

            # temp makes sure the possible no of subarray in the middle
            temp = prefix_sum - k
            if temp in freq:
                result += freq[temp]

            # if the temp not in freq, insert the prefix_sum in map
            # even if temp in freq, we need to increase the frequency of the prefix_sum
            # as we are encounted this prefix_sum in the past 
            freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

        return result

        # TC: O(n^2), SC: O(1) => TLE
        # count = 0

        # for i in range(len(nums)):
        #     temp = 0
        #     for j in range(i, len(nums)):
        #         temp += nums[j]
        #         if temp == k:
        #             count += 1
        # return count