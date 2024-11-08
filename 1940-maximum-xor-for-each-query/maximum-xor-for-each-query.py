# the issue is we can not just compute xor for all possible k, we need to find k such that
# the selected k maximize the (xor_nums ^ k). In this case, what we need to do is to select k as
# a number that differs from xor_nums value as much bit positions as possible.
# The best approach is to flip all bits of xor_nums within a fixed bit range. This means using a 
# k that has 1s where xor_nums has 0s and vice versa, up to the bit limit.

# a ^ b ^ c = total_xor
# total_xor ^ c = a ^ b
class Solution:    
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        result = []
        length = len(nums)

        xor_nums = 0
        for n in nums:
            xor_nums ^= n  

        # it is guranteed that the maximized xor will be 2^(maximumBit) - 1
        # because of "0 <= nums[i] < 2^maximumBit" this constraint
        # creates a binary number with exactly k bits sets to '1'
        max_possible_xor = (1 << maximumBit) - 1

        for _ in range(length):
            max_k = xor_nums ^ max_possible_xor
            result.append(max_k)
            last_val = nums.pop()
            # update xor_nums by performing xor with the popped element and the previous xor
            xor_nums = xor_nums ^ last_val

        return result


# TC: O(n*2^maximumBit + n^2) => TLE
# class Solution:
#     def computeListXOR(self, nums: List[int]) -> int:
#         ans = 0
#         for n in nums:
#             ans ^= n
#         return ans
    
#     def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
#         result = []
#         k_list = []
#         max_xor = 0
        
#         # constructing k_list to store the all possible values of k (1 to 2^maxbit)
#         for k in range(0, pow(2, maximumBit)):
#             k_list.append(k)
        
#         while len(nums) > 0:
#             xor_num = self.computeListXOR(nums)
#             for k in k_list:
#                 # if the xor of nums is 0, the max_k will maximize the xor, no need to compute max_xor
#                 if xor_num == 0:
#                     max_k = k_list[-1]
#                     break
#                 max_xor = max(max_xor, xor_num ^ k)
#                 if max_xor == xor_num ^ k:
#                     max_k = k
#             result.append(max_k)
#             max_xor = 0
#             nums.pop()

#         return result
