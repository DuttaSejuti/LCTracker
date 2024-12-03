class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        new_str = ''
        k = 0
        start = 0

        while k < len(spaces): # O(k)
            end = spaces[k]
            for i in range(start, end, 1): # O(m)
                new_str += s[i]
            new_str += ' '
            start = end # new start will be the ending index
            k += 1

        return new_str + s[end:]
