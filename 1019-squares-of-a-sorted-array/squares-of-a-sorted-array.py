class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        max_num = max(-(nums[0]),nums[-1])
        new_list = [[] for i in range(0, max_num+1)]
        res = list()

        for n in nums:
            if n < 0:
                n = -(n)
            new_list[n].append(n)

        for n in new_list:
            if not n:
                continue
            val = n[0]
            n_size = len(n)
            while(n_size>0):
                res.append(val*val)
                n_size -= 1

        return res