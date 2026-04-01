class Solution:
    def isHappy(self, n: int) -> bool:
        digits = [int(d) for d in str(n)]
        seen = set()

        while True:
            sum_digit = 0
            if n in seen:
                return False
            else:
                seen.add(n)

            for digit in digits:
                sum_digit += digit * digit
            if sum_digit == 1:
                return True
            digits = [int(d) for d in str(sum_digit)]
            n = sum_digit

        return False



        