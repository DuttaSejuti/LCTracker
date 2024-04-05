class Solution:
    def makeGood(self, s: str) -> str:
        stack = list()
        
        for i in range(len(s)):
            if stack and (s[i].islower() and s[i].upper() == stack[-1]):
                stack.pop()
            elif stack and (s[i].isupper() and s[i].lower() == stack[-1]):
                stack.pop()
            else:
                stack.append(s[i])
                
        return ''.join(stack)

    # def makeGood(self, s: str) -> str:
    #     stack = []
    #     for char in list(s):
    #         if stack and abs(ord(char) - ord(stack[-1])) == 32:
    #             stack.pop()
    #         else:
    #             stack.append(char)
    #     return "".join(stack)