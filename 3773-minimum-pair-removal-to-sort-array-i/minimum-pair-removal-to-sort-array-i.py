class Solution:
    def is_sorted(self, nums: List[int]) -> bool:
        is_sorted = all(nums[i] <= nums[i+1] for i in range(len(nums)-1))
        return is_sorted
    
    def pair_sum(self, nums:List[int]) -> Tuple[List[int], int]:
        length = len(nums)
        sum_list = [0]*(length-1)
        min_val = float("inf")

        for i in range(length-1):
            pair_sum = nums[i] + nums[i+1]
            sum_list[i] = pair_sum
            min_val = min(min_val, pair_sum)
        
        return sum_list, min_val

    def find_first_min_val_pair_position(self, sum_pair: List[int], min_val: int) -> int:
        for i in range(len(sum_pair)):
            if sum_pair[i] == min_val:
                return i
    
    def perform_the_operation(self, nums: List[int], first_min_val_pair: int, min_val: int) -> List[int]:
        new_nums = nums[:first_min_val_pair+1] + nums[first_min_val_pair+2:]
        new_nums[first_min_val_pair] = min_val

        return new_nums

    def minimumPairRemoval(self, nums: List[int]) -> int:
        if self.is_sorted(nums):
            return 0
        
        min_operation = 0
        while True:
            sum_pair, min_val = self.pair_sum(nums)
            first_min_val_pair = self.find_first_min_val_pair_position(sum_pair, min_val)
            new_nums = self.perform_the_operation(nums, first_min_val_pair, min_val)
            min_operation += 1
            if self.is_sorted(new_nums):
                break
            nums = new_nums
        
        return min_operation
        