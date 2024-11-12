class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for bit in range(32):
            bit_mask = 1 << bit
            if n & bit_mask > 0:
                count += 1
        return count
