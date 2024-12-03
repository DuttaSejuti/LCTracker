# O(n) => Optimized
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        start = 0
        
        for space in spaces:
            result.append(s[start:space])
            result.append(' ')
            start = space
        
        result.append(s[start:])
        return ''.join(result)

# O(n^2) => Brute Force
# class Solution:
#     def addSpaces(self, s: str, spaces: List[int]) -> str:
#         new_str = ''
#         k = 0
#         start = 0

#         while k < len(spaces): # O(m)
#             end = spaces[k]
#             for i in range(start, end, 1): # O(n)
#                 new_str += s[i] # this one creates a new string; O(k)
#             new_str += ' '
#             start = end # new start will be the ending index
#             k += 1

#         return new_str + s[end:]
