class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        pointer_s, pointer_t = 0, 0

        while pointer_s < len(s) and pointer_t < len(t):
            while pointer_s < len(s) and pointer_t < len(t) and s[pointer_s] == t[pointer_t]:
                pointer_s += 1
                pointer_t += 1
            pointer_s += 1
        return len(t) - (pointer_t)
