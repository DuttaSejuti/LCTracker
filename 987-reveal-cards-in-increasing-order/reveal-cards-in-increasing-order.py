# we have x = [17,13,11,2,3,5,7], we know the function which is the simulation on the queue
# after the simulation the result f(x)=y, where y = [17,11,3,7,2,13,5]
# now, we know what order we want f(x')=y', where y' =[2,3,5,7,11,13,17]
# the x' of that function would be the result
# x = [17,13,11,2,3,5,7]
     # 0, 1, 2, 3 4,5,6
# y = [17,11,3,7,2,13,5]
      # 0, 2,4,6,3,1,5
# y' = [2,3,5,7,11,13,17]
    #    0, 2,4,6,3,1,5
# x' = [2,13,3,11,5,17,7]
      #  0,1,2, 3,4, 5,6
# after performing the simulation on x = [17,13,11,2,3,5,7], the indices of the array changes in the y
# y = [17,11,3,7,2,13,5] => [0,2,4,6,3,1,5]
# for the second one, y = [2,3,5,7,11,13,17] => [2,3,5,7,11,13,17]
# if we take the indices to it's initial stage, we get x = [0,1,2,3,4,5,6] => [2,13,3,11,5,17,7] => result
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deckIdxQueue = deque()
        hashMap = dict()
        resultIdx = list()

        # initializeQueueWithIndices
        for i in range(len(deck)):
            deckIdxQueue.append(i)
        
        # perform the simulation on deckIdxQueue till queue becomes empty
        # append the revealed cardIdx in the result
        while deckIdxQueue:
            curr = deckIdxQueue.popleft()
            if deckIdxQueue:
                next_curr = deckIdxQueue.popleft()
                deckIdxQueue.append(next_curr)
            resultIdx.append(curr)

        # the order we want
        deck.sort()
        
        # mapping the desiredDeck's element to the resultIdx {element: idx}
        for i, deck in enumerate(deck):
            hashMap[deck] = resultIdx[i]
        
        # sorting the map to get the correct order 0, 1, 2, 3
        hashMap = dict(sorted(hashMap.items(), key = lambda x: x[1]))

        # the sorted map's key would be the answer
        return list(hashMap.keys())
