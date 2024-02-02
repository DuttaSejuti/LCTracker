class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sequential_digits_nums_list = list()
        result = list()
        l,r = 0,1
        standard_str = '123456789'

        for i in range(len(standard_str)):
            while l < r and r < 9:
                sequential_digits_nums_list.append(int(standard_str[l:r+1]))
                l += 1
                r += 1
            l = 0
            r = i + 2
        
        for n in sequential_digits_nums_list:
            if n >= low and n <= high:
                result.append(n)
        return result

        #TLE => O(n^2)
        # result = list()

        # for num in range(low, high+1, 1):
        #     str_num = str(num)

        #     for i in range(len(str_num)-1):
        #         if int(str_num[i+1]) != int(str_num[i])+1:
        #             break
        #         if i == len(str_num)-2:
        #             result.append(num)

        # return result
