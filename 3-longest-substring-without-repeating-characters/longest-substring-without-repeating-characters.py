class Solution:
    # TC: O(n), SC: O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        length, max_length = 0, 0
        freq = dict()

        for r in range(len(s)):
            char = s[r]
            freq[char] = freq.get(char, 0) + 1

            while freq.get(char, 0) > 1:
                freq[s[l]] -= 1
                l += 1
            max_length = max(max_length, r-l+1)

        return max_length


    # TC: O(n^2),  SC: O(n) => Brute Force; AC anyway
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     max_length, length = 0, 0
    #     freq = dict()

    #     for i in range(len(s)):
    #         freq = dict()
    #         length = 0
    #         for j in range(i, len(s)):
    #             char = s[j]
    #             freq[char] = freq.get(char, 0) + 1
    #             if freq.get(char, 0) > 1:
    #                 break
    #             else:
    #                 length += 1
    #             max_length = max(max_length, length)

    #     return max_length

