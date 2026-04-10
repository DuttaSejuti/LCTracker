class Solution:
    # TC: O(n) SC: O(n)
    def minimumDistance(self, nums: List[int]) -> int:
        freq_map = defaultdict(list)
        min_distance = float('inf')

        for i, num in enumerate(nums):
            freq_map[num].append(i)
        
        for k, v in freq_map.items():
            if len(v) >= 3:
                for i in range(0, len(v) - 2, 1):
                    # no abs(), as the indices are appended in the dict in sorted manner
                    # temp_distance = (v[i+1]-v[i]) + (v[i+2]-v[i+1]) + (v[i+2]-v[i])

                    # 2 * (max_index - min_index)  {2*(k-i)} for any three indices
                    temp_distance = 2 * (v[i+2] - v[i])
                    min_distance = min(temp_distance, min_distance)

        if min_distance == float('inf'): return -1

        return min_distance
