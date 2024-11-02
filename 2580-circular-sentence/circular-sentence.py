# TC: O(n). SC: O(n)
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(' ')
        prev = words[0][-1] # last char of the first word
        for i in range(1, len(words)):
            if words[i][0] != prev:
                return False
            prev = words[i][-1]
        
        return True if prev == words[0][0] else False # check for the last word and the first one

# TC: O(n), SC: O(1)
# class Solution:
#     def isCircularSentence(self, sentence: str) -> bool:
#         for i in range(len(sentence)):
#             if sentence[i] == ' ' and sentence[i - 1] != sentence[i + 1]:
#                 return False
#         return sentence[0] == sentence[len(sentence) - 1]