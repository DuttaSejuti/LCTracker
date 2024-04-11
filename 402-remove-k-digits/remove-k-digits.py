class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = list()

        for i in range(len(num)):
            curr = num[i]
            while stack and stack[-1] > curr and k > 0:
                stack.pop()
                k -= 1
            stack.append(curr)
        
        # after removing the larger peak values, if k remains
        # if the input is in sorted-order, remove from the end
        while k:
            stack.pop()
            k -= 1
        
        res = ''.join(stack).lstrip('0') # remove leading zeros from left

        if res:
            return res
        else:
            return '0'
