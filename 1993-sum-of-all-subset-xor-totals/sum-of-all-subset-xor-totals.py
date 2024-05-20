class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def get_all_subsets(num_list):
            subset_list = []
            for i in range(len(num_list) + 1):
                subset_list.extend(combinations(num_list, i))

            subsets = []
            for subset in subset_list:
                subsets.append(list(subset))
            return subsets
        
        subsets = get_all_subsets(nums)

        total_xor = 0
        xor = 0
        for subset in subsets:
            xor = 0
            for i in range(len(subset)):
                xor ^= subset[i]
            total_xor += xor
        return total_xor
