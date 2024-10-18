class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ele_idx_pair = []
        rank_dict = {}
        result = [0] * len(arr)
        
        # keep track of the original index
        for i in range(len(arr)):
            ele_idx_pair.append((arr[i], i))
        
        arr.sort()
        rank = 1
        for i in range(len(arr)):
            if rank_dict.get(arr[i]) != None:
                continue
            rank_dict[arr[i]] = rank
            rank += 1
        
        for pair in ele_idx_pair:
            result[pair[1]] = rank_dict[pair[0]]
        
        return result
    