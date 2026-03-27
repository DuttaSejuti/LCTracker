from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        result = []
        length = len(nums)
        for num, count in freq.items():
            if count > (length//3):
                result.append(num)
        return result
