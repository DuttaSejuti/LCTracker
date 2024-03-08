# IDEA
# Get the frequency of the elements in a dictionary, get the max from the values of the dict
# sum the values of the keys, whose value == max_val
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # TC:O(n) SC:O(n)
        freq = dict()
        count = 0
        max_freq = 0
        
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        # max_v = max(freq.values())
        # the upper line is doing this under the hood
        for f in freq.values():
            max_freq = max(f, max_freq)

        for f in freq.keys():
            if freq.get(f) == max_freq:
                count += max_freq
                
        return count
        