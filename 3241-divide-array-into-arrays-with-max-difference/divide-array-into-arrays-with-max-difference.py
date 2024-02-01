class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        s_nums = sorted(nums)
        result = []
        flag = 0

        for i in range(0, len(s_nums)-2, 3):
            result.append([s_nums[i], s_nums[i+1], s_nums[i+2]])
        
        for array in result:
            if array[1] - array[0] <= k and array[2] - array[1] <= k and array[2] - array[0] <= k:
                flag = 1
            else:
                flag = 0
                break

        if flag == 1:
            return result
        else:
            return []
