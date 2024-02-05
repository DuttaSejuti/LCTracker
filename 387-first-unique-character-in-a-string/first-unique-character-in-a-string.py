class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_list = [0]*26
        for char in s:
            char_list[ord(char) - ord('a')] += 1
        
        for i in range(len(s)):
            if char_list[ord(s[i]) - ord('a')] == 1:
                return i
        return -1

        #TC:O(n) SC: O(n)
        # new_dict = dict()
        # for char in s:
        #     new_dict[char] = new_dict.get(char, 0) + 1
        
        # for i in range(len(s)):
        #     if new_dict.get(s[i]) == 1:
        #         return i
        # return -1
   