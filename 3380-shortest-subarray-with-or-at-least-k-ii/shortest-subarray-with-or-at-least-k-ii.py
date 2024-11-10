# two pointers for constructing sub-arrays
# think it like a sub_array sum >= k type of problem
class Solution:
    def addCounter(self, num: int, counter_list: List[int]) -> None:
        for bit in range(32):
            bit_mask = 1 << bit
            if bit_mask & num != 0:
                counter_list[bit] += 1

    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        or_sum = 0
        min_length = float(inf) # because we want to get the min, to minimize the effect, we choose a big value
        setBitCounter = [0]*32

        while r < len(nums):
            or_sum |= nums[r]
            
            self.addCounter(nums[r], setBitCounter)
            # fail condition
            while l <= r and r < len(nums) and or_sum >= k:
                for bit in range(32):
                    bit_mask = 1 << bit
                    if nums[l] & bit_mask != 0:
                        setBitCounter[bit] -= 1
                    if setBitCounter[bit] == 0:
                        # unset a bit position of or_sum
                        or_sum = or_sum & ~bit_mask
               
                min_length = min(min_length, r-l+1)
                l+= 1

            r += 1

        return min_length if min_length != float(inf) else -1
