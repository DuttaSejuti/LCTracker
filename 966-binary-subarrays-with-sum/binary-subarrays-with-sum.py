class Solution:
    def numSubarraysWithSum(self, array: List[int], goal: int) -> int:
        freq = dict()
        freq[0] = 1
        result = 0
        currSum = 0

        for i in range(len(array)):
            currSum += array[i]
            diff = currSum - goal

            result += freq.get(diff, 0)
            freq[currSum] = freq.get(currSum, 0) + 1

        return result