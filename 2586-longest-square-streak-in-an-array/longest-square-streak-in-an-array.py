class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        # nums.sort(reverse = True)
        freq = dict()
        result = []
        min_value = 1.00001
    
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        for n in nums:
            temp = set()
            while n > min_value:
                # print("N", n)
                s = math.sqrt(n)
                # print("S", s)
                if freq.get(s, 0) != 0 and freq.get(n, 0) != 0: # exists in the nums
                    if n not in temp:
                        temp.add(n)
                    if s not in temp:
                        temp.add(s)
                n = math.sqrt(n)
                # print(temp)
            # print(temp)
            if len(temp) > 1:
                result.append(len(temp))

        return max(result) if len(result) > 0 else -1
