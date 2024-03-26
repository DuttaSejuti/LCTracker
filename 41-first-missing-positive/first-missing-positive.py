class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        new_dict = dict()

        for n in nums:
            new_dict[n] = new_dict.get(n, 0) + 1
        
        i = 1
        while i:
            if i not in new_dict:
                return i
            i += 1
        