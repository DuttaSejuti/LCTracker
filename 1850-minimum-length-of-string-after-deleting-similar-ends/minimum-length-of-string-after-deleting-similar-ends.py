class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s) - 1

        while l < r and s[l] == s[r]:
            while l < r and s[l] == s[l+1]:
                l += 1
            while l < r and s[r] == s[r-1]:
                r -= 1

            s = s[l+1:r]
            l, r = 0, len(s) - 1

        return len(s)
