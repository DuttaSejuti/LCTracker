class Solution:
    # def firstMissingPositive(self, nums: List[int]) -> int:


    # Basic Solution
    # to know what elements are in the array, we use dictionary, then a basic for loop in range(1, len(nums) + 1),
    # that will return when i is not present in the dictionary

    # (.) zero(0) is not a positive integer here
    # (.) we have used dictinary instead of checking i in nums because dictionary search will take O(1), but list search will take O(n)
    # TC:O(n), SC:O(n) => AC
    def firstMissingPositive(self, nums: List[int]) -> int:
        new_dict = dict()

        for n in nums:
            new_dict[n] = new_dict.get(n, 0) + 1
        
        # len(nums) + 2 because, in the worst case i can be len(nums) + 1, +2 to make i len(nums) + 1 inclusive
        # suppose nums = [1,2,3], here result will be 4 which is len(nums) + 1
        for i in range(1, len(nums) + 2):
            if i not in new_dict:
                return i

