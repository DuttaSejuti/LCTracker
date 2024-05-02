class Solution:
    # store all the elements in a dictionary
    # for all the keys, if the opposite key exists in the dict, calculate the max
    # TC: O(n), SC:O(n)
    def findMaxK(self, nums: List[int]) -> int:
        new_dict = dict()
        max_ele = -1

        for n in nums:
            new_dict[n] = new_dict.get(n, 0) + 1
        
        for k in new_dict:
            if -k in new_dict:
                max_ele = max(max_ele, abs(k))
        
        return max_ele
