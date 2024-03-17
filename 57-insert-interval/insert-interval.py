# IDEA
# Possible cases:


class Solution:
    # check if the two interval overlaps or not and build a array of 0 and 1
    def checkOverlap(self, currentInt: List[int], newInt: List[int]) -> int:
        # overlap exists if the newInt ends before the start of the currentInt or
        # newInt starts after the end of the currentInt
        if currentInt[0] > newInt[1] or currentInt[1] < newInt[0]:
            return 0
        return 1
    
    def mergeInterval(self, intervals: List[List[int]], newInterval: List[int], checkOverlapList: List[int]) -> List[List[int]]:
        result = list()

        for i in range(len(intervals)):
            currentInt = intervals[i]
            if checkOverlapList[i] == 0:
                result.append(currentInt)
            else:
                newInterval[0] = min(currentInt[0], newInterval[0])
                newInterval[1] = max(currentInt[1], newInterval[1])

                if i == len(intervals) - 1 or checkOverlapList[i+1] == 0:
                    result.append(newInterval)

        return result

            
    def insertInterval(self, intervals: List[List[int]], newInterval: List[int], checkOverlap: List[int]) -> List[List[int]]:
        result = list()
        modifiedIntervals = [[-1,-1]]

        for i in range(len(intervals)):
            modifiedIntervals.append(intervals[i])
        
        modifiedIntervals.append([math.inf, math.inf])

        for i in range(1, len(modifiedIntervals)):
            print("haha")
            prev = modifiedIntervals[i-1]
            curr = modifiedIntervals[i]

            if prev[1] < newInterval[0] and curr[0] > newInterval[1]:
                result.append(newInterval)
            if i != len(modifiedIntervals) - 1:
                result.append(curr)

        return result


    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        checkOverlapList = list()
        mergeInterval = 0

        # construct the list to check where is the overlap occurs [0,1,1,1,0] or [0,0,0,0]
        for i in range(len(intervals)):
            res = self.checkOverlap(intervals[i], newInterval)
            # mergeInterval = res | mergeInterval
            if res == 1:
                mergeInterval = 1
            checkOverlapList.append(res)
        
        if mergeInterval:
            return self.mergeInterval(intervals, newInterval, checkOverlapList)
        
        return self.insertInterval(intervals, newInterval, checkOverlapList)

