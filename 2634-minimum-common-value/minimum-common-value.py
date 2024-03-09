class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        new_dict = dict()
        for n1 in nums1:
            new_dict[n1] = new_dict.get(n1, 0) + 1

        for n2 in nums2:
            if new_dict.get(n2):
                return n2
        return -1