class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0

        for word in words:
            l, r = 0, 0
            while l < len(word) and r < len(pref):
                if word[l] != pref[r]:
                    break
                if r == len(pref) - 1 and word[l] == pref[r]:
                    count += 1
                l += 1
                r += 1
        return count

# class Solution:
#     def prefixCount(self, words: List[str], pref: str) -> int:
#         count = 0
#         for word in words:
#             if word.startswith(pref):
#                 count += 1
#         return count
