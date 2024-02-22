class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ans = int()
        for i in range(31, -1, -1):
            if left&(1<<i) != right&(1<<i):
                break
            ans |= left&(1<<i)
        return ans

        # max_bits = max(left.bit_length(), right.bit_length())
        # left = bin(left)[2:].zfill(max_bits)
        # right = bin(right)[2:]
        # ans = ''

        # for i in range(max_bits):
        #     if left[i] != right[i]:
        #         break
        #     ans += left[i]

        # if not ans:
        #     return 0
        # else:
        #     ans += '0' * (max_bits - len(ans))

        # return int(ans, 2)

        # ans = left
        # for i in range(left+1, right+1, 1):
        #     ans &= i
        # return ans
      