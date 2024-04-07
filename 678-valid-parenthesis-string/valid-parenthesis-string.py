class Solution:
    def checkValidString(self, s: str) -> bool:
        dp = dict()
        pos, count = 0, 0

        def checkValid(pos, count) -> bool:
            if count < 0: # if count is negative, no need to go ahead, already invalid
                return False

            if pos == len(s): # base: end of the string
                return count == 0
            
            if dp.get((pos, count)) != None: # dp[(pos, count)] exists
                return dp[(pos, count)]
            
            if s[pos] == '(':
                res = checkValid(pos+1, count+1)
            if s[pos] == ')':
                res = checkValid(pos+1, count-1)
            if s[pos] == '*':
                res = (checkValid(pos+1, count+1) # '('
                or checkValid(pos+1, count-1) # ')'
                or checkValid(pos+1, count)) # ''

            dp[(pos, count)] = res

            return res

        return checkValid(pos, count)
