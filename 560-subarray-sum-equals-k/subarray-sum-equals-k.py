class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        ps = 0
        # prefix_sum = dict()
        prefix_sum_count = dict()
        prefix_sum_count[0] = 1
        for i in range(len(nums)):
            ps += nums[i]
            # prefix_sum[i] = ps
            # if ps == k:
            #     count += 1

            known_variable = (ps - k) 
            
            count += prefix_sum_count.get(known_variable, 0)

            prefix_sum_count[ps] = prefix_sum_count.get(ps, 0) + 1

            # for j in range(0, i):
            #     condition = (prefix_sum[j] == known_variable)
            #     # condition = (prefix_sum[i] - prefix_sum[j] == k)
            #     count += condition
        return count


        # TC: O(n), SC: O(n)
        # freq = dict() # prefix_sum: # of occurances of this currSum
        # freq[0] = 1 # to resolve the case where we get currSum = 0 in future
        # result = 0
        # currSum = 0

        # for i in range(len(nums)):
        #     currSum += nums[i]

        #     # if we chop of a prefix of diff from the subarray we will get a subarray of k
        #     diff = currSum - k

        #     # this is basically checking if the diff in the map ot not, if present get the freq
        #     result += freq.get(diff, 0)

        #     # we need to check if we have encountered the diff previously, the prefix_sum that we need to chop off from the subarray
        #     freq[currSum] = freq.get(currSum, 0) + 1

        # return result

        # TC: O(n^2), SC: O(1) => TLE
        # count = 0

        # for i in range(len(nums)):
        #     temp = 0
        #     for j in range(i, len(nums)):
        #         temp += nums[j]
        #         if temp == k:
        #             count += 1
        # return count