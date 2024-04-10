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

# another way without indices
#  x = [17,13,11,2,3,5,7]
#  y = [17,11,3,7,2,13,5]
#  y'= [2,3,5,7,11,13,17]
# {17:2, 11:3, 3:5....}
# apply the same mapping to the given deck
#  x' = [2,13,3,11,5,17,7]

class Solution:
    # TC:O(nlogn), SC:O(n)
   def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deckQueue = deque()
        result = list()
        hashMap = dict()

        # convert the given list into queue for performing the simulation
        for d in deck:
            deckQueue.append(d)
    
        # perform the simulation on the queue and get the result 
        while deckQueue:
            curr = deckQueue.popleft()
            if deckQueue:
                curr_next = deckQueue.popleft()
                deckQueue.append(curr_next)
            result.append(curr)
        
        # the order of the deck we want
        desired_result = sorted(deck)

        # map the result value to the desired_value {result_val:sorted_desired_val}
        for i,e in enumerate(result):
            hashMap[e] = desired_result[i]
        
        final_result = list()

        # apply the mapping to the given deck
        for d in deck:
            mapped_val = hashMap[d]
            final_result.append(mapped_val)

        return final_result
        
    # def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
    #     deckIdxQueue = deque()
    #     hashMap = dict()
    #     resultIdx = list()

    #     # initializeQueueWithIndices
    #     for i in range(len(deck)):
    #         deckIdxQueue.append(i)
        
    #     # perform the simulation on deckIdxQueue till queue becomes empty
    #     # append the revealed cardIdx in the result
    #     while deckIdxQueue:
    #         curr = deckIdxQueue.popleft()
    #         if deckIdxQueue:
    #             next_curr = deckIdxQueue.popleft()
    #             deckIdxQueue.append(next_curr)
    #         resultIdx.append(curr)

    #     # the order we want
    #     deck.sort()
        
    #     # mapping the desiredDeck's element to the resultIdx {element: idx}
    #     for i, deck in enumerate(deck):
    #         hashMap[deck] = resultIdx[i]
        
    #     # sorting the map to get the correct order 0, 1, 2, 3
    #     hashMap = dict(sorted(hashMap.items(), key = lambda x: x[1]))

    #     # the sorted map's key would be the answer
    #     return list(hashMap.keys())
