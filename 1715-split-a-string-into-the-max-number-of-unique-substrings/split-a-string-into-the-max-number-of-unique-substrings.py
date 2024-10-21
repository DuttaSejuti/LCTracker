# TC: O(n*2^n)
# SC: O(n)
class Solution:
    def backtrack(self, pos: int, s: str, hashSet: set) -> int:
        if pos == len(s):
            return len(hashSet)
            # return 0 # if used 1 + function call

        maxCount = 0
        for i in range(pos, len(s)):
            sub = s[pos:i+1]
            if sub not in hashSet:
                hashSet.add(sub)
                maxCount = max(maxCount, self.backtrack(i+1, s, hashSet))
                # maxCount = max(maxCount, 1 + self.backtrack(i+1, s, hashSet)) # if base case returned 0
                hashSet.remove(sub)
        return maxCount
        
            
    def maxUniqueSplit(self, s: str) -> int:
        pos = 0
        hashSet = set()

        return self.backtrack(0, s, hashSet)
        