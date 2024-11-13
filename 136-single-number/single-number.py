# if we xor 2 same number, we get zero, as we have only 1 element that does not appear twice
# performing xor on all the elements will result in zero for the duplicate numbers, (0 xor number that appears once = single_sumber)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        return xor
