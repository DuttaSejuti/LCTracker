class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3: return False

        increaseStart = False
        decreaseStart = False


        for i in range(0, len(arr)-1):
            if arr[i] == arr[i+1]: return False

            if arr[i] < arr[i+1]:
                increaseStart = True
                if not decreaseStart and i != len(arr)-2:
                    continue
                else:
                    return False
            if arr[i] > arr[i+1]:
                decreaseStart = True
                if increaseStart:
                    continue
                else:
                    return False
        return True #if increaseStart and decreaseStart else False
          