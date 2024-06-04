class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_freq = dict()
        odd_flag = 0
        longest_palindrome_len = 0

        for char in s:
            char_freq[char] = char_freq.get(char, 0) + 1
        
        for freq in char_freq:
            if char_freq[freq] % 2 != 0:
                if odd_flag == 0:
                    odd_flag = 1
                else:
                    char_freq[freq] -= 1
            longest_palindrome_len += char_freq[freq]

        return longest_palindrome_len
