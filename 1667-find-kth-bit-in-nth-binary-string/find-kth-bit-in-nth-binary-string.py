class Solution:
    def invertNum(self, n: str) -> str:
        res = ''
        for i in range(len(n)):
            if n[i] == '0':
                res += '1'
            else:
                res += '0'
        return res

    def nthBinaryString(self, n: int) -> str:
        if(n == 1): return "0"

        s = self.nthBinaryString(n-1)

        return s + "1" + self.invertNum(s)[::-1]


    def findKthBit(self, n: int, k: int) -> str:
        return self.nthBinaryString(n)[k-1]