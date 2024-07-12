class Solution:
    # TC:O(logn), SC:O(1)
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        mid = 0

        # we need to check equal l<=r, because there can be only one element [5] and target is 5
        # then l and l are same, without equal, this will return -1, will not go insode the loop
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return - 1

    # TC:O(n), SC:O(n)
    # def search(self, nums: List[int], target: int) -> int:
    #     new_dict = dict()
    #     for i in range(len(nums)):
    #         new_dict[nums[i]] = i
    #         if nums[i] == target:
    #             return i
    #     return -1
       