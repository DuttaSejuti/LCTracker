class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()
        for n in nums:
            if n in hashSet:
                return True
            hashSet.add(n)
        return False

        # new_dict = dict()
        # for element in nums:
        #     #None means the dict does not have the key now, if the value != None
        #     # this means we already have this key in the dict
        #     if new_dict.get(element) != None:
        #         return True
        #     else:
        #         new_dict[element] = 1
        # return False
                    