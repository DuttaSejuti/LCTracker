class Solution:
    def countSubarraysWhereTargetExistsAtLeastKTimes(self, nums: List[int], k: int, target: int) -> int:
        # TC:O(n), SC:O(1)
        l, r = 0, 0
        result = 0
        count = 0
        n = len(nums)

        for r in range(len(nums)):
            if nums[r] == target:
                count += 1
            while l <= r and count == k:
                if nums[l] == target:
                    count -= 1

                # this makes sure that the window itself a valid subarray
                # plus all the subarrays with the rest of the right elemets are also valid
                result += n - r
                l += 1

            # similarly this will work instead of result += n-r
            # result += l
        return result

    def breakdownList(self, nums: List[int], minK: int, maxK: int) -> List[List[int]]:
        new_list = []

        l, r = 0, 0

        while l < len(nums):
            while r < len(nums) and minK <= nums[r] <= maxK:
                r += 1
            # no valid subarray
            if l == r:
                r += 1
            else:
                new_list.append(nums[l:r])
            l = r
        return new_list

    def countSubarraysWhereTargetExists(self, valid_list: List[int], target: int, left_boundary: int, right_boundary: int) -> int:
        valid_lists = self.breakdownList(valid_list, left_boundary, right_boundary)

        count = 0
        for valid_list in valid_lists:
            count += self.countSubarraysWhereTargetExistsAtLeastKTimes(valid_list, 1, target)
        return count

    def countSubarraysWhereMaxExists(self, valid_list: List[int], target: int, boundary: int) -> int:
        valid_lists = self.breakdownList(valid_list, boundary + 1, target)

        count = 0
        for valid_list in valid_lists:
            count += self.countSubarraysWhereTargetExistsAtLeastKTimes(valid_list, 1, target)
        return count
    
    def countSubarraysWhereMinExists(self, valid_list: List[int], target: int, boundary: int) -> int:
        valid_lists = self.breakdownList(valid_list, target, boundary - 1)

        count = 0
        for valid_list in valid_lists:
            count += self.countSubarraysWhereTargetExistsAtLeastKTimes(valid_list, 1, target)
        return count
    
    def countSubarrayWhereNoneExists(self, valid_list: List[int], minK: int, maxK: int) -> int:
        valid_lists = self.breakdownList(valid_list, minK + 1, maxK - 1)

        count = 0
        for valid_list in valid_lists:
            valid_list_length = len(valid_list)
            count += (valid_list_length * (valid_list_length + 1)) // 2

        return count

    def countValidSubarrays(self, valid_list: List[int], minK: int, maxK: int) -> int:
        length = len(valid_list)
        total_subarray = (length * (length + 1)) // 2

        # max_exists = self.countSubarraysWhereMaxExists(valid_list, maxK, minK)
        # min_exists = self.countSubarraysWhereMinExists(valid_list, minK, maxK)

        max_exists = self.countSubarraysWhereTargetExists(valid_list, maxK, minK + 1, maxK)
        min_exists = self.countSubarraysWhereTargetExists(valid_list, minK, minK, maxK - 1)


        none_exists = self.countSubarrayWhereNoneExists(valid_list, minK, maxK)

        # print(max_exists, min_exists, none_exists)

        return total_subarray - (max_exists + min_exists + none_exists)

    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        valid_lists = self.breakdownList(nums, minK, maxK)

        count = 0
        for valid_list in valid_lists:
            count += self.countValidSubarrays(valid_list, minK, maxK)

        return count