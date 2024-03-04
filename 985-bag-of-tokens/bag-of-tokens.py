# IDEA
# 1) sorting the tokens, as we want to lose power with the lowest token to gain score,
# and lose score to gain highest power so that we can use that power to score more..
# 2) two pointers => l tracking the lowest tokens; r tracking the highest tokens
# l++ => till we can lose power and gain score; power--, score++
# r-- => if we have tokens[i] > power, we can not lose power, but if score > 0,
#        we can gain power by losing score; power++, score--

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        max_score = 0
        score = 0
        t_size = len(tokens)
        l, r = 0, t_size - 1 # to track lowest and highest tokens
        tokens.sort()

        if(l == r and tokens[l] <= power):
            return 1

        while(l < r):
            while(l <= r and tokens[l] <= power):
                power -= tokens[l]
                score = score + 1
                max_score = max(max_score, score)
                l += 1
            if score > 0:
                score = score - 1
                max_score = max(max_score, score)
                power += tokens[r]
                r -= 1
            else:
                l += 1

        return max_score
