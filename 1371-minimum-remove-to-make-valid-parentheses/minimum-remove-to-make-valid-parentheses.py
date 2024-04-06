class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = list()
        idx_map = dict()
        res = ''

        for i in range(len(s)):
            if stack and s[i] == ')' and stack[-1] == '(':
                stack.pop()
                idx_map.popitem()
            elif s[i] == '(' or s[i] == ')':
                stack.append(s[i])
                idx_map[i] = 1
        
        for i in range(len(s)):
            if i not in idx_map:
                res += s[i]
        
        return res
        
        
            
