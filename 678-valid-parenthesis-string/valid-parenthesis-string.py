class Solution:
    def checkValidString(self, s: str) -> bool:
        dp = dict()
        pos, count = 0, 0

        def checkValid(pos, count) -> bool:
            if count < 0:
                return False 

            if pos == len(s):
                if count == 0:
                    return True
                else:
                    return False
            
            if dp.get((pos, count)) != None:
                return dp[(pos, count)]
            
            if s[pos] == '(':
                res = checkValid(pos+1, count+1)
            if s[pos] == ')':
                res = checkValid(pos+1, count-1)
            if s[pos] == '*':
                res = (checkValid(pos+1, count+1)
                or checkValid(pos+1, count-1)
                or checkValid(pos+1, count))

            dp[(pos, count)] = res

            return res

        return checkValid(pos, count)
