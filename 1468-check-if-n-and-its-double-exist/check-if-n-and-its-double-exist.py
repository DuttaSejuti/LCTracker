class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        new_dict = dict()
        for i in range(len(arr)):
            new_dict[arr[i]] = i 

        for i in range(len(arr)):
            double = arr[i] * 2
            if double in new_dict and i != new_dict.get(double, 0):
                return True
        return False
