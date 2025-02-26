class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        # parity = 0 => even, parity = 1 => odd
        prev_parity = (nums[0] % 2) #first element's parity

        for i in range(1, len(nums)):
            curr_parity = nums[i] % 2
            # if the two adjacent parity is equal, they are not different
            if curr_parity == prev_parity:
                return False
            prev_parity = curr_parity

        return True