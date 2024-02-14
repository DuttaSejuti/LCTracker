class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result = []
        posNum = []
        negNum = []

        for i in range(len(nums)):
            if nums[i] > 0:
                posNum.append(nums[i])
            else:
                negNum.append(nums[i])
        
        for i in range(len(posNum)):
            result.append(posNum[i])
            result.append(negNum[i])

        return result
