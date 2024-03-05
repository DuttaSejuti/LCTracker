class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s) - 1

        while l < r  and s[l] == s[r]:
            c = s[l] # get the first char of the string

            # delete consecutive c from the prefix
            # <= is used when we have "cabaabac", at the end we have "aa"
            while l <= r and s[l] == c:
                l += 1

            # delete consecutive c from the suffix
            while l < r and s[r] == c:
                r -= 1

        return r-l+1


        # Not good as we are modifing the string
        # l, r = 0, len(s) - 1

        # while l < r and s[l] == s[r]:
        #     while l < r and s[l] == s[l+1]:
        #         l += 1
        #     while l < r and s[r] == s[r-1]:
        #         r -= 1

        #     s = s[l+1:r]
        #     l, r = 0, len(s) - 1

        # return len(s)
