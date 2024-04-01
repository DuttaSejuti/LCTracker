class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new_list = s.strip().split(' ')
        return len(new_list[-1])
