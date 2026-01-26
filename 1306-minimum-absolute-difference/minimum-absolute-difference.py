class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        pair_index_dict = defaultdict(list)
        min_diff = float('inf')
        arr.sort()
        result_array = []

        print(arr)
        for i in range(len(arr)-1):
            abs_diff = abs(arr[i]-arr[i+1])
            if min_diff >= abs_diff:
                pair_index_dict[abs_diff].append(i)
                min_diff = abs_diff
        
        pairs = pair_index_dict[min_diff]
        for i in range(len(pairs)):
            result_array.append([arr[pairs[i]], arr[pairs[i]+1]])
        
        return result_array