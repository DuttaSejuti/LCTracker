class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        minKIndex, maxKIndex, culpritIndex = -1, -1, -1
        temp = 0

        for i in range(len(nums)):
            # valid elements in the range of minK and maxK are considered in the subarray
            if minK <= nums[i] <= maxK:
                if nums[i] == minK:
                    minKIndex = i
                if nums[i] == maxK:
                    maxKIndex = i
            # elements out of the range is considered culprit
            else:
                culpritIndex = i

            temp = min(minKIndex, maxKIndex) - culpritIndex
            
            if temp >= 0: # temp can be negative
                ans += temp
            
        return ans

    # Modular solution
    # def countSubarraysWhereTargetExistsAtLeastKTimes(self, nums: List[int], k: int, target: int) -> int:
    #     # TC:O(n), SC:O(1)
    #     l, r = 0, 0
    #     result = 0
    #     count = 0
    #     n = len(nums)

    #     for r in range(len(nums)):
    #         if nums[r] == target:
    #             count += 1
    #         while l <= r and count == k:
    #             if nums[l] == target:
    #                 count -= 1

    #             # this makes sure that the window itself a valid subarray
    #             # plus all the subarrays with the rest of the right elemets are also valid
    #             result += n - r
    #             l += 1

    #         # similarly this will work instead of result += n-r
    #         # result += l
    #     return result

    # def breakdownList(self, nums: List[int], minK: int, maxK: int) -> List[List[int]]:
    #     new_list = []

    #     l, r = 0, 0

    #     while l < len(nums):
    #         while r < len(nums) and minK <= nums[r] <= maxK:
    #             r += 1
    #         # no valid subarray
    #         if l == r:
    #             r += 1
    #         else:
    #             new_list.append(nums[l:r])
    #         l = r
    #     return new_list

    # # Generalized function of the underlying 2 functions
    # # It returns count of all subarrays where a target exists between a range
    # def countSubarraysWhereTargetExists(self, valid_list: List[int], target: int, left_boundary: int, right_boundary: int) -> int:
    #     valid_lists = self.breakdownList(valid_list, left_boundary, right_boundary)

    #     count = 0
    #     for valid_list in valid_lists:
    #         count += self.countSubarraysWhereTargetExistsAtLeastKTimes(valid_list, 1, target)
    #     return count

    # def countSubarraysWhereMaxExists(self, valid_list: List[int], target: int, boundary: int) -> int:
    #     valid_lists = self.breakdownList(valid_list, boundary + 1, target)

    #     count = 0
    #     for valid_list in valid_lists:
    #         count += self.countSubarraysWhereTargetExistsAtLeastKTimes(valid_list, 1, target)
    #     return count
    
    # def countSubarraysWhereMinExists(self, valid_list: List[int], target: int, boundary: int) -> int:
    #     valid_lists = self.breakdownList(valid_list, target, boundary - 1)

    #     count = 0
    #     for valid_list in valid_lists:
    #         count += self.countSubarraysWhereTargetExistsAtLeastKTimes(valid_list, 1, target)
    #     return count
    
    # def countSubarrayWhereNoneExists(self, valid_list: List[int], minK: int, maxK: int) -> int:
    #     valid_lists = self.breakdownList(valid_list, minK + 1, maxK - 1)

    #     count = 0
    #     for valid_list in valid_lists:
    #         valid_list_length = len(valid_list)
    #         count += (valid_list_length * (valid_list_length + 1)) // 2

    #     return count

    # def countValidSubarrays(self, valid_list: List[int], minK: int, maxK: int) -> int:
    #     length = len(valid_list)
    #     total_subarray = (length * (length + 1)) // 2

    #     max_exists = self.countSubarraysWhereMaxExists(valid_list, maxK, minK)
    #     min_exists = self.countSubarraysWhereMinExists(valid_list, minK, maxK)

    #     # This is just calling the generalized function with the boundaries in the parameter
    #     # max_exists = self.countSubarraysWhereTargetExists(valid_list, maxK, minK + 1, maxK)
    #     # min_exists = self.countSubarraysWhereTargetExists(valid_list, minK, minK, maxK - 1)


    #     none_exists = self.countSubarrayWhereNoneExists(valid_list, minK, maxK)

    #     # print(max_exists, min_exists, none_exists)

    #     return total_subarray - (max_exists + min_exists + none_exists)

    # def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
    #     valid_lists = self.breakdownList(nums, minK, maxK)

    #     count = 0
    #     for valid_list in valid_lists:
    #         count += self.countValidSubarrays(valid_list, minK, maxK)

    #     return count