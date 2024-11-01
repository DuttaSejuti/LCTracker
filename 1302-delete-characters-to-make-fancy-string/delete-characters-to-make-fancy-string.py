class Solution:
    def makeFancyString(self, s: str) -> str:
        result = []
        count = 0
        c = '#' # for checking the first char

        for char in s:
            if char == c:
                count += 1
            else:
                c = char
                count = 1
            if count < 3:
                result.append(char)

        return ''.join(result)

# class Solution:
#     def makeFancyString(self, s: str) -> str:
#         result = []
#         if len(s) <=2 : return s

#         for i in range(len(s)-2):
#             a, b, c = s[i], s[i+1], s[i+2]

#             if a != b or b != c or a != c:
#                 result.append(a)

#             if i == len(s) - 3:
#                 result.append(b)
#                 result.append(c)

#         return ''.join(result)
