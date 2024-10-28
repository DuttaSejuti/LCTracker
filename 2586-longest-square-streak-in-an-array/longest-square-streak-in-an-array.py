class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        freq = dict()
        result = [0]
        min_value = 1.00001
    
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        for n in nums:
            temp = set()
            while n > min_value:
                s = math.sqrt(n)
                if freq.get(s, 0) != 0 and freq.get(n, 0) != 0: # exists in the nums
                        temp.add(n)
                        temp.add(s)
                n = math.sqrt(n)
            if len(temp) > 1:
                max_len = max(result[-1], len(temp))
                result.append(max_len)

        return result[-1] if result[-1] != 0 else -1

# class Solution:
#     def longestSquareStreak(self, nums: List[int]) -> int:
#         longestStreak = 0
#         nums = set(nums) # we can access in set in O(1) times

#         for n in nums:
#             currentStreak = 0
#             square_root = n
#             while square_root in nums:
#                 currentStreak += 1
#                 if square_root * square_root > 10**5:
#                     break
#                 square_root *= square_root
#             longestStreak = max(longestStreak, currentStreak)
#         return longestStreak if longestStreak >= 2 else -1

