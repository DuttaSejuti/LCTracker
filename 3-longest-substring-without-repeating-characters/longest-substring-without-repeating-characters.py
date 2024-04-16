class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length, length = 0, 0
        freq = dict()

        for i in range(len(s)):
            freq = dict()
            length = 0
            for j in range(i, len(s)):
                char = s[j]
                freq[char] = freq.get(char, 0) + 1
                if freq.get(char, 0) > 1:
                    break
                else:
                    length += 1
                max_length = max(max_length, length)

        return max_length

