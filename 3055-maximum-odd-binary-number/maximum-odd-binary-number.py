class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        # consider zero_count and zero_one; LSB would be 1 for odd numbers
        # max number would have the max no of 1 at the front

        res = ''
        zero_count = 0
        one_count = 0
    
        for i in s:
            if i == '0':
                zero_count +=1
            else:
                one_count += 1
        
        res += (one_count - 1) * '1'
        res += zero_count * '0'
        res += '1'

        return res

        # TLE
        # numbers = set()
        # perms = permutations(s)

        # for perm in perms:
        #     num = ''.join(perm)
        #     if num[-1] == '1':
        #         numbers.add(num)

        # return sorted(numbers)[-1]