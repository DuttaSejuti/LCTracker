class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for c in s:
            if c in t:
                idx = t.index(c) 
                t = t[idx+1:]
            else:
                return False        
        return True