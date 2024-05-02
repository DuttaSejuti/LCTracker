class Solution:
    # store all the elements in a dictionary
    # for all the keys, if the opposite key exists in the dict, calculate the max
    # TC: O(n), SC:O(n) => 2 pass
    def findMaxK(self, nums: List[int]) -> int:
        new_dict = dict()
        max_ele = -1

        for n in nums:
            new_dict[n] = new_dict.get(n, 0) + 1
        
        for k in new_dict:
            if -k in new_dict:
                max_ele = max(max_ele, abs(k))
        
        return max_ele

# TC:O(n), SC:O(n) => 1 pass
# class Solution:
#     def findMaxK(self, nums: List[int]) -> int:
#         ans = -1

#         # A set to store seen numbers
#         seen = set()

#         for num in nums:
#             abs_num = abs(num)

#             # If the absolute value is greater than the current maximum and its negation is seen
#             if abs_num > ans and -num in seen:
#                 ans = abs_num
#             seen.add(num)  # Insert the current number into the set

#         return ans