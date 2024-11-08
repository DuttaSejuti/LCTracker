# the issue is we can not just compute xor for all possible k, we need to find k such that
# the selected k maximize the (xor_nums ^ k). In this case, what we need to do is to select k as
# a number that differs from xor_nums value as much bit positions as possible.
# The best approach is to flip all bits of xor_nums within a fixed bit range. This means using a 
# k that has 1s where xor_nums has 0s and vice versa, up to the bit limit.

# a ^ b ^ c = total_xor
# total_xor ^ c = a ^ b

# solution with assuming the max_xor will be (1<<maximumbit)-1
# class Solution:    
#     def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
#         result = []
#         length = len(nums)

#         xor_nums = 0
#         for n in nums:
#             xor_nums ^= n  

#         # it is guranteed that the maximized xor will be 2^(maximumBit) - 1
#         # because of "0 <= nums[i] < 2^maximumBit" this constraint
#         # creates a binary number with exactly k bits sets to '1'
#         max_possible_xor = (1 << maximumBit) - 1

#         for _ in range(length):
#             max_k = xor_nums ^ max_possible_xor
#             result.append(max_k)
#             last_val = nums.pop()
#             # update xor_nums by performing xor with the popped element and the previous xor
#             xor_nums = xor_nums ^ last_val

#         return result

class Solution:
    def getComplementXOR(self, xor_nums: int, maximumBit: int) -> int:
        max_k = 0
        for bit in range(maximumBit):
            mask = 1 << bit
            # check if the bit at position "bit" in xor_nums is 0; if so, set that bit in max_k
            if xor_nums & mask == 0:
                max_k |= mask
        return max_k

    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        result = []
        length = len(nums)

        xor_nums = 0
        for n in nums:
            xor_nums ^= n
        
        for _ in range(length):
            max_k = self.getComplementXOR(xor_nums, maximumBit) # basically flipped_xor
            result.append(max_k)
            last_val = nums.pop()
            xor_nums = xor_nums ^ last_val
        
        return result
