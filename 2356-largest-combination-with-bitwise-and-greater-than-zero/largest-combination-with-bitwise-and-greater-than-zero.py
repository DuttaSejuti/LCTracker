# TC: O(n), SC: O(n)
# we will filter out the numbers from the candidates, that have 
class Solution:
    def getLength(self, candidates: List[int], bit_pos: int) -> int:
        bit_mask = 1 << bit_pos # for bit pos 0, bit_mask will be .....001; 1 at position 0

        # we filter the numbers in candidates that has '1' at bit pos "bit_pos"
        filtered_subset = [num for num in candidates if num & bit_mask]

        return len(filtered_subset)

    def largestCombination(self, candidates: List[int]) -> int:
        max_length = 0
        bit_pos_length = {} # bit_pos : length => 0:3; at bit position 0 is 1, the size of the subset 
        
        for bit_pos in range(24): # 0 to 23, because 10^7 means at most 24 bits are needed to represent any candidate
            bit_pos_length[bit_pos] = self.getLength(candidates, bit_pos)
            max_length = max(max_length, bit_pos_length[bit_pos])
        
        return max_length


# TC: O(n*2^n) => MLE
# class Solution:
#     def getCombinations(self, candidates: List[int]) -> List[List[int]]:
#         subset_list = []
#         for i in range(len(candidates) + 1):
#             subset_list.extend(combinations(candidates, i))
        
#         subsets = [list(subset) for subset in subset_list]
#         return subsets
    
#     def checkNonzeroAnd(self, array: List[int]) -> bool:
#         ans = array[0]
#         for n in array[1:]:
#             ans &= n
#             if ans == 0:
#                 return False
#         return True

#     def largestCombination(self, candidates: List[int]) -> int:
#         combinations = self.getCombinations(candidates)
#         max_length = 0

#         for combination in combinations:
#             if len(combination) > 0 and self.checkNonzeroAnd(combination):
#                 max_length = max(max_length, len(combination))
        
#         return max_length

