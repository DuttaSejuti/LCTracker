#IDEA
# get the nums1 array in a dictionary, for iterating over num2, check if new_dict.get[n2], return n2
# as the numbers are sorted, if we get a common element, no need to find the rest common
# we only need to return the lowest common number
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # with Two pointers
        # TC: O(n+m), SC: O(1)
        first, second = 0, 0
        l1, l2 = len(nums1), len(nums2)

        while first < l1 and second < l2:
            if nums1[first] == nums2[second]:
                return nums1[first]
            elif nums1[first] < nums2[second]:
                first += 1
            else: # nums1[first] > nums2[second]
                second += 1
        return -1

        # with Set intersection
        # set1 = set(nums1)
        # set2 = set(nums2)
        # common = set1.intersection(set2)

        # if common:
        #     return min(common)
        # else:
        #     return -1

        # With HashMap
        # TC: O(n+m), SC:O(n)
        # new_dict = dict()
        # for n1 in nums1:
        #     new_dict[n1] = new_dict.get(n1, 0) + 1

        # for n2 in nums2:
        #     if new_dict.get(n2):
        #         return n2
        # return -1