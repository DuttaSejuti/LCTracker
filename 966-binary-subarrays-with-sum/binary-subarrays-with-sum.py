class Solution:
    def numSubarraysWithSum(self, array: List[int], goal: int) -> int:
        # using sliding window
        # Example : [0, 0, 0, 1, 1] -> Total subarrays having goal = 2 will be 4 - {0, 0, 0, 1, 1},  {0, 0, 1, 1}, {0, 1, 1}, {1, 1}
        # So, simply find the count of zeros before the sum has reached goal i.e. 3 (Now, 1+1 = goal, so total subarrays = prefix_zeros + 1 = 3 + 1 = 4)
        #  TC: O(n), SC: O(1)
        l, r = 0, 0
        currSum = 0
        result = 0
        count_zero = 0

        while r < len(array):
            currSum += array[r]

            while l < r and (array[l] == 0 or currSum > goal):
                if array[l] == 0:
                    count_zero += 1
                else:
                    count_zero = 0
                currSum -= array[l]
                l += 1
        
            if currSum == goal:
                result += 1 + count_zero
            
            r += 1

        return result

        # Same to same as LC:560
        # freq = dict()
        # freq[0] = 1
        # result = 0
        # currSum = 0

        # for i in range(len(array)):
        #     currSum += array[i]
        #     diff = currSum - goal

        #     result += freq.get(diff, 0)
        #     freq[currSum] = freq.get(currSum, 0) + 1

        # return result