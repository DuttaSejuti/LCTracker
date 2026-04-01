class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ele_idx = defaultdict(list)
        for i in range(len(nums)):
            ele_idx[nums[i]].append(i)
        
        for _, v in ele_idx.items():
            equal_found = len(v)
            if equal_found > 1:
                for i in range(1, equal_found):
                    if abs(v[i-1]-v[i]) <= k:
                        return True
        return False