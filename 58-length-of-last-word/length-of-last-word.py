class Solution:
    # TC:O(n), SC:O(n)
    # def lengthOfLastWord(self, s: str) -> int:
    #     new_list = s.strip().split(' ')
    #     return len(new_list[-1])
    
    def lengthOfLastWord(self, s: str) -> int:
        size = len(s) - 1
        len_count = 0
        while size >= 0:
            if s[size] != ' ':
                len_count += 1
            if s[size] == ' ' and len_count > 0:
                break
            
            size -= 1
        
        return len_count
