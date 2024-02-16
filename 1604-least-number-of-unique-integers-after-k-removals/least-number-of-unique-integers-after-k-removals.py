class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        new_dict = dict()

        for n in arr:
            new_dict[n] = new_dict.get(n, 0) + 1
        
        sorted_new_dict = dict(sorted(new_dict.items(), key = lambda x:x[1]))
        
        for key in sorted_new_dict:
            if sorted_new_dict[key] <= k:
                k = k - sorted_new_dict[key]
                del new_dict[key]
            else:
                k = k - sorted_new_dict[key]
                if k < 0:
                    break
        return len(new_dict)
