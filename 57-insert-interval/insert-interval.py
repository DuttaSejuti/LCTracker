class Solution:
    # TC: O(n), SC: O(n)
    # check if the two interval overlaps or not and build an array of 0 and 1
    def checkOverlap(self, currentInt: List[int], newInt: List[int]) -> int:
        # no-overlap if the newInt ends before the start of the currentInt or
        # newInt starts after the end of the currentInt
        if currentInt[0] > newInt[1] or currentInt[1] < newInt[0]:
            return 0
        return 1
    
    def mergeInterval(self, intervals: List[List[int]], newInterval: List[int], checkOverlapList: List[int]) -> List[List[int]]:
        result = list()

        for i in range(len(intervals)):
            currentInt = intervals[i]
            if checkOverlapList[i] == 0: # no-overlap
                result.append(currentInt)
            else: # overlap exits
                # merging the intervals to get the newInterval
                newInterval[0] = min(currentInt[0], newInterval[0])
                newInterval[1] = max(currentInt[1], newInterval[1])

                # if we are at the end of the intervals or the newInt doesn't overlap with the next interval
                # append the modified newInterval
                if i == len(intervals) - 1 or checkOverlapList[i+1] == 0:
                    result.append(newInterval)

        return result

    # no overlap 
    def insertInterval(self, intervals: List[List[int]], newInterval: List[int], checkOverlap: List[int]) -> List[List[int]]:
        result = list()
        # newInterval can be inserted in three positions
        # i) at the beginning, ii) at the end, iii) in between 2 intervals
        # to generalize and use the 3rd case for all we insert the dummy interval at the start [-1,-1]
        modifiedIntervals = [[-1,-1]]
        
        # insert the actual given intervals
        for i in range(len(intervals)):
            modifiedIntervals.append(intervals[i])
        
        # insert dummy [inf, inf] at the end
        modifiedIntervals.append([math.inf, math.inf])

        for i in range(1, len(modifiedIntervals)):
            prev = modifiedIntervals[i-1]
            curr = modifiedIntervals[i]
            
            # to find the place where newInterval is in between 2 intervals
            if prev[1] < newInterval[0] and curr[0] > newInterval[1]:
                result.append(newInterval)
            # we have to take the curr always as it's our given interval
            if i != len(modifiedIntervals) - 1:
                result.append(curr)

        return result


    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        checkOverlapList = list()
        # a flag to determine if there is an overlap between the intervals and the newInterval or not
        # if overlap occurs, we have to merge the newInterval to the exiting intervals, otherwise just inter the newInterval
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

