class Solution:
    def firstUniqChar(self, s: str) -> int:
        new_dict = dict()
        for char in s:
            new_dict[char] = new_dict.get(char, 0) + 1
        
        for i in range(len(s)):
            if new_dict.get(s[i]) == 1:
                return i
        return -1
   