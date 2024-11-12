class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            if n & 1 > 0:
                count += 1
            n >>= 1 # right shift n by 1 bit
        return count

# O(1)
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         count = 0
#         for bit in range(32):
#             bit_mask = 1 << bit
#             if n & bit_mask > 0:
#                 count += 1
#         return count


# Brian Kernighan's algorithm
# class Solution:
#     def hammingWeight(self, num: int) -> int:
#         count = 0
#         while num:
#             num &= (num-1)
#             count += 1
#         return count


