class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False

        increaseStart = False
        decreaseStart = False

        for i in range(n - 1):
            if arr[i] == arr[i + 1]:  # Check for equal elements
                return False

            if arr[i] < arr[i + 1]:
                if decreaseStart:  # If we have started decreasing, it's invalid
                    return False
                increaseStart = True  # We have started increasing

            elif arr[i] > arr[i + 1]:  # If current is greater than next
                decreaseStart = True  # We have started decreasing

        # We need both increase and decrease to have a valid mountain
        return increaseStart and decreaseStart

# class Solution:
#     def validMountainArray(self, arr: List[int]) -> bool:
#         if len(arr) < 3: return False

#         increaseStart = False
#         decreaseStart = False

#         for i in range(0, len(arr)-1):
#             if arr[i] == arr[i+1]: return False # numbers can not be equal

#             if arr[i] < arr[i+1]:
#                 increaseStart = True
#                 # increase can occur till we find find any decreaseStart
#                 # if we are at the end and still neven find decreaseStart, then no mountain, False
#                 if not decreaseStart and i != len(arr)-2:
#                     continue
#                 else:
#                     return False
#             if arr[i] > arr[i+1]:
#                 decreaseStart = True
#                 # we can only find decrease if we have already found increaseStart
#                 if increaseStart:
#                     continue
#                 else:
#                     return False
#         return True

#         # add "if increaseStart and decreaseStart else False" in the last return statement
#         # if you do not add "and i!=len(arr)-2"

# # Another easy to understand Solution
# class Solution:
#     def validMountainArray(self, arr: List[int]) -> bool:
#         if len(arr) < 3:
#             return False
        
#         i = 0
#         n = len(arr)
        
#         # Climb up
#         while i < n - 1 and arr[i] < arr[i + 1]:
#             i += 1

#         # Peak can't be the first or last element
#         if i == 0 or i == n - 1:
#             return False

#         # Climb down
#         while i < n - 1 and arr[i] > arr[i + 1]:
#             i += 1

#         # If we reach the end, it's a valid mountain
#         return i == n - 1