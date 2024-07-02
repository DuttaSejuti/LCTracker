class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = list()
        new_dict = dict()

        for n1 in nums1:
            new_dict[n1] = new_dict.get(n1, 0) + 1

        for n2 in nums2:
            if n2 in new_dict and new_dict.get(n2) > 0:
                res.append(n2)
                new_dict[n2] -= 1
        return res
