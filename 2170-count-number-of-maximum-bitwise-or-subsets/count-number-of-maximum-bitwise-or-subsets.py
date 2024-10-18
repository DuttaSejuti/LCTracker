class Solution:
    def computeOR(self, arr: List[int]) -> int:
        if len(arr) == 0:
            return 0

        result = arr[0] # initialize with first element
        for num in arr[1:]:
            result |= num # perform bitwise or with each element
        return result # cumulative or result
    
    def generateSubsets(self, arr: List[int]) -> List[int]:
        subset_list = []
        for i in range(len(arr) + 1):
                subset_list.extend(combinations(arr, i)) # this generates tuples [(), (1), (2), (1,2)]
        
        subsets = [list(subset) for subset in subset_list] # converting tuples to list [[], [1], [2], [1,2]]
        return subsets
    
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = self.computeOR(nums)
        subsets = self.generateSubsets(nums)
        result = 0

        for subset in subsets:
            if self.computeOR(subset) == max_or:
                result += 1
        
        return result
