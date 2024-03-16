class Solution:
    def getNextSequence(self, n: str) -> str:
        count = 1
        res = ''

        for i in range(len(n)-1):
            if(n[i] == n[i+1]):
                count += 1
            else:
                res += str(count)
                res += n[i]
                count = 1

        res += str(count)
        res += n[-1]

        return res

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        return self.getNextSequence(self.countAndSay(n-1))
        
        # alternative of recursion
        # for i in range(n):
        #     res = self.getNextSequence(res)
        
        # return res
        

            