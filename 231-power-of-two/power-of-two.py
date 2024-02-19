class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # TC:O(1), SC:O(1)
        # TC is O(1) because the no of iterations is contant
        for i in range(31):
            power = 2 ** i
            if n == power:
                return True
        return False
    
        # TC: O(logn) SC: O(1)
        # if n <= 0: return False
        # while n > 1:
        #     if n % 2 != 0:
        #         return False
        #     n = n//2
        # return True
