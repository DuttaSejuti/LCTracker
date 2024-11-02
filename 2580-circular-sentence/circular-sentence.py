class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(' ')
        prev = words[0][-1] # last char of the first word
        for i in range(1, len(words)):
            if words[i][0] != prev:
                return False
            prev = words[i][-1]
        
        return True if prev == words[0][0] else False 
