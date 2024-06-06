# [1,2,3,6,2,3,4,7,8]
# => [1,2,2,3,3,4,6,7,8]
# {1:1, 2:2, 3:2, 6:1, 4:1, 7:1, 8:1}
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq = dict()
        
        if len(hand) % groupSize != 0:
            return False
        for n in hand:
            freq[n] = freq.get(n, 0) + 1
        hand.sort()
        for n in hand:
            if freq[n] > 0:
                for i in range(n, n+groupSize):
                    if freq.get(i, 0) == 0:
                        return False
                    freq[i] -= 1
        return True                 
