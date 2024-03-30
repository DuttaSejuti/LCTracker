class Solution:
    def subarraysWithAtMostK(self, nums: List[int], k: int) -> int:
        count = 0
        l, r = 0, 0
        new_dict = dict()

        for r in range(len(nums)):
            num = nums[r]
            new_dict[num] = new_dict.get(num, 0) + 1

            while len(new_dict) > k:
                num = nums[l]
                new_dict[num] -= 1
                if new_dict[num] == 0:
                    del new_dict[num]
                l += 1

            count += r-l+1

        return count

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.subarraysWithAtMostK(nums, k) - self.subarraysWithAtMostK(nums, k-1)
