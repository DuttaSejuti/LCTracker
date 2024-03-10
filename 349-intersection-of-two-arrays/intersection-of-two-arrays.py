class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # TC: O(n+m), SC:O(n)
        new_dict = dict()
        res = list()

        for n1 in nums1:
            new_dict[n1] = 1
        
        for n2 in nums2:
            # check if n2 is in n1/dict and n2 already in result array;
            if n2 in new_dict and new_dict[n2] == 1:
                res.append(n2)
                new_dict[n2] = 0 # so that duplicate number can't append in res array

        return res

        # # TC: O(n+m), SC: O(n+m)
        # set1 = set(nums1)
        # set2 = set(nums2)

        # common = set1.intersection(set2)

        # return list(common)
        