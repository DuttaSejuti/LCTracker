class Solution:
    def kPositive(self, code: List[int], k: int, result: List[int]) -> List[int]:
        copy_k = k
        for i in range(len(code)):
            j = i + 1
            while k:
                if j > len(code) - 1:
                    j = 0
                result[i] += code[j]
                k -= 1
                j += 1
            k = copy_k
        return result
    
    def kNegative(self, code: List[int], k: int, result: List[int]) -> List[int]:
        copy_k = k
        for i in range(len(code)):
            j = i - 1
            while k:
                if j < 0:
                    j = len(code) - 1
                result[i] += code[j]
                k -= 1
                j -= 1
            k = copy_k
        return result

    def decrypt(self, code: List[int], k: int) -> List[int]:
        result = [0]*len(code)
        if k == 0: return result
        if k > 0:
            return self.kPositive(code, k, result)
        else:
            return self.kNegative(code, -k, result)
        