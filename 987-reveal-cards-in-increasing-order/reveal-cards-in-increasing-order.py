class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deckQueue = deque()
        result = list()
        hashMap = dict()

        for d in deck:
            deckQueue.append(d)
    
        while deckQueue:
            curr = deckQueue.popleft()
            if deckQueue:
                curr_next = deckQueue.popleft()
                deckQueue.append(curr_next)
            result.append(curr)
        
        desired_result = sorted(deck)

        for i,e in enumerate(result):
            hashMap[e] = desired_result[i]
        
        final_result = list()

        for d in deck:
            mapped_val = hashMap[d]
            final_result.append(mapped_val)

        return final_result

