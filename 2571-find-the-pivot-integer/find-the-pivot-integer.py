# IDEA
# approach 1) construst the array from 1 to n, take two sum, one from 1 to i, another 1 to n,
            # if they are equal we have found the pivot

class Solution:
    def pivotInteger(self, n: int) -> int:
        nums = list()
        sum_from_1 = 0 # calculating sum from 1 to i
        sum_from_i = 0 # calculating sum from i to n

        # construct the list in range 1 to n inclusive
        for i in range(1, n+1):
            nums.append(i)

        for i in range(len(nums)):
            sum_from_1 += nums[i]
            for j in range(i, len(nums)):
                sum_from_i += nums[j]
            if sum_from_1 == sum_from_i:
                return nums[i]
            sum_from_i = 0 # as we need to calculate the sum once again
        return -1
