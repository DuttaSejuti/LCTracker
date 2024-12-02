# binary search solution => TC: O(nlogn); SC: O(n)
class Solution:
    def binarySearch(self, arr: List[int], target: int) -> int:
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1

    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(len(arr)):
            double = 2 * arr[i] 
            idx = self.binarySearch(arr, double)
            # checks if the target exists and it's not the same index
            if idx >= 0 and idx != i:
                return True
        return False

# 1 pass with HashSet => TC: O(n), SC: O(n)
# class Solution:
#     def checkIfExist(self, arr: List[int]) -> bool:
#         hashSet = set()

#         for num in arr:
#             if num * 2 in hashSet or (num % 2 == 0 and num // 2 in hashSet):
#                 return True
#             hashSet.add(num)
#         return False

# 2 pass with Hash Map => TC: O(n), SC: O(n)
# class Solution:
#     def checkIfExist(self, arr: List[int]) -> bool:
#         new_dict = dict()
#         for i in range(len(arr)):
#             new_dict[arr[i]] = i 

#         for i in range(len(arr)):
#             double = arr[i] * 2
#             if double in new_dict and i != new_dict.get(double, 0):
#                 return True
#         return False
