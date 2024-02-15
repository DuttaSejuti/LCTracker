class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # iii
        hashSet = set()
        for n in nums:
            if n in hashSet:
                return True
            hashSet.add(n)
        return False

        # ii
        # new_dict = dict()
        # for element in nums:
        #     #None means the dict does not have the key now, if the value != None
        #     # this means we already have this key in the dict
        #     if new_dict.get(element) != None:
        #         return True
        #     else:
        #         new_dict[element] = 1
        # return False

        # i
        # new_dict = dict()
        # for element in nums:
        #     new_dict[element] = new_dict.get(element, 0) + 1
        # for v in new_dict.values():
        #     if v > 1:
        #         return True
        # return False
