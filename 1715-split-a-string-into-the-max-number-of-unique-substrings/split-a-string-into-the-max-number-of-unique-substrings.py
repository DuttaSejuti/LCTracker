class Solution:
    def backtrack(self, pos: int, s: str, hashSet: set) -> int:
        if pos == len(s):
            return len(hashSet)

        maxCount = 0
        for i in range(pos, len(s)):
            sub = s[pos:i+1]
            if sub not in hashSet:
                hashSet.add(sub)
                maxCount = max(maxCount, self.backtrack(i+1, s, hashSet))
                hashSet.remove(sub)
        return maxCount
        
            
    def maxUniqueSplit(self, s: str) -> int:
        pos = 0
        currCount = 0
        hashSet = set()

        return self.backtrack(0, s, hashSet)
        