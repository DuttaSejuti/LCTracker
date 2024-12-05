class Solution:
    def canChange(self, start: str, target: str) -> bool:
        start_length = len(start)
        l, r = 0, 0

        while l < start_length or r < start_length:
            while l < start_length and start[l] == "_": l += 1

            while r < start_length and target[r] == "_": r += 1

            if l == start_length or r == start_length:
                return l == start_length and r == start_length

            if start[l] != target[r] or (start[l] == "L" and l < r) or (start[l] == "R" and l > r):
                return False

            l += 1
            r += 1

        return True