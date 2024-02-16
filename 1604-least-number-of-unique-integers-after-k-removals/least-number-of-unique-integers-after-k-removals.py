class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        new_dict = dict()
        count = 0

        for n in arr:
            new_dict[n] = new_dict.get(n, 0) + 1
        
        new_dict = dict(sorted(new_dict.items(), key = lambda x:x[1]))
        
        for key in new_dict:
            if new_dict[key] <= k:
                k = k - new_dict[key]
                # del new_dict[key]
                count += 1
            else:
                k = k - new_dict[key]
                if k < 0:
                    break

        return len(new_dict) - count
