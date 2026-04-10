class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        freq_map = defaultdict(list)
        min_distance = float('inf')

        for i, num in enumerate(nums):
            freq_map[num].append(i)
        
        for k, v in freq_map.items():
            if len(v) >= 3:
                for i in range(0, len(v)-2, 1):
                    temp_distance = abs(v[i]-v[i+1]) + abs(v[i+1]-v[i+2]) + abs(v[i+2]-v[i])
                    min_distance = min(temp_distance, min_distance)

        if min_distance == float('inf'): return -1

        return min_distance