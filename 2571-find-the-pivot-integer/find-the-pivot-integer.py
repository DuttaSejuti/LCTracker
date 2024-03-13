# IDEA
# approach 1) construst the array from 1 to n, take two sum, one from 1 to i, another 1 to n,
            # if they are equal we have found the pivot
# approach 2) construct prefix sum list, looping from 1 to n, 

class Solution:
    def pivotInteger(self, n: int) -> int:
        # using maths
        # TC: O(1), SC:O(1)
        # total_sum = n*(n+1)//2
        # pivot = int(math.squt(total_sum))

        # if pivot * pivot == total_sum:
        #     return pivot
        # else:
        #     return -1

        # Binary Search
        # TC: O(logn), SC: O(1)
        left, right = 1, n
        total_sum = n*(n+1)//2
        
        while left < right:
            mid = (left+right) // 2

            if mid*mid - total_sum < 0:
                left = mid + 1
            else:
                right = mid
        
        if left * left == total_sum:
            return left
        else:
            return -1

        # TC: O(n), SC: O(1)
        # sum_from_1 = 0
        # total_sum = n*(n+1) // 2

        # for i in range(1, n+1):
        #     sum_from_1 += i
        #     if sum_from_1 == total_sum - (sum_from_1 - i):
        #         return i
        # return -1

        # TC: O(n), SC: O(n)
        # prefix_sum = [0]
        
        # # constructing the prefix_sum
        # for i in range(1, n+1):
        #     prefix_sum.append(prefix_sum[i-1]+i)

        # last_sum = prefix_sum[-1] #similar as n(n+1)//2

        # for i in range(1, n+1):
        #     if prefix_sum[i] == (last_sum - prefix_sum[i-1]):
        #         return i
        # return -1

        # TC: O(n^2), SC: O(n)
        # nums = list()
        # sum_from_1 = 0 # calculating sum from 1 to i
        # sum_from_i = 0 # calculating sum from i to n

        # # construct the list in range 1 to n inclusive
        # for i in range(1, n+1):
        #     nums.append(i)

        # for i in range(len(nums)):
        #     sum_from_1 += nums[i]
        #     for j in range(i, len(nums)):
        #         sum_from_i += nums[j]
        #     if sum_from_1 == sum_from_i:
        #         return nums[i]
        #     sum_from_i = 0 # as we need to calculate the sum once again
        # return -1
