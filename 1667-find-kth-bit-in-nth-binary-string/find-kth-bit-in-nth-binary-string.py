class Solution:
    def invertNum(self, n: str) -> str:
        res = ''
        for i in range(len(n)):
            if n[i] == '0':
                res += '1'
            else:
                res += '0'
        return res

    def findKthBit(self, n: int, k: int) -> str:
        num = "0"
        if n == 1: return num

        for i in range(n-1):
            tmp = num
            num += "1"
            num += self.invertNum(tmp)[::-1]
        
        return num[k-1]


