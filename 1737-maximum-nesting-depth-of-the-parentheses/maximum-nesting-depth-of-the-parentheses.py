class Solution:
    # TC: O(n), SC:O(1)
    # def maxDepth(self, s: str) -> int:
    #     count = 0
    #     max_depth = 0

    #     for i in range(len(s)):
    #         if s[i] == '(':
    #             count += 1
    #             max_depth = max(max_depth, count) # count will only increase here
    #         if s[i] == ')':
    #             count -= 1

    #         # max_depth = max(max_depth, count)
    #     return max_depth

    # TC: O(n), SC:O(n)
    def maxDepth(self, s: str) -> int:
        ans = 0
        stack = list()

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
                ans = max(ans, len(stack))
            if s[i] == ')':
                stack.pop()

        return ans
