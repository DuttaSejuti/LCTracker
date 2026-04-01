class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        disappear_num = []
        result_set = set(range(1, len(nums)+1))
        given_set = set(nums)
        for num in result_set:
            if num not in given_set:
                disappear_num.append(num)
        return disappear_num
        