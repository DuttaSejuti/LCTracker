class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        cycle = 'abcdefghijklmnopqrstuvwxyz'
        l, r = 0, 0
        match_count = 0
        cycle_length = len(cycle)

        while l < len(str1):
            if str1[l] == str2[r]:
                match_count += 1
                r += 1
            else:
                current_index = cycle.index(str1[l])
                new_index = (current_index + 1) % cycle_length
                if cycle[new_index] == str2[r]:
                    match_count += 1
                    r += 1
            
            if r == len(str2): # this means r has incremented to len(str2); all the mayching are found
                return True if match_count == len(str2) else False

            l += 1

        return True if match_count == len(str2) else False