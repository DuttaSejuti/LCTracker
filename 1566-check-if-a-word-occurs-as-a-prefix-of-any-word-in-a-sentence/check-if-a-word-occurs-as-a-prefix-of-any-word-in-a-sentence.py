# TC: O(n*k); SC:O(1)
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        wordPos, idx = 1, 0
        
        while idx < len(sentence):
            if sentence[idx: idx + len(searchWord)] == searchWord:
                # boundary check, if the substring is the start of the word
                # if i == 0, do not have to check for space, that's why or
                if idx == 0 or sentence[idx-1] == ' ':
                    return wordPos
            if sentence[idx] == ' ':
                wordPos += 1
            idx += 1

        return -1
            

# TC: O(n*m); SC:O(n)
# class Solution:
#     def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
#         words = sentence.split(' ')

#         for i in range(len(words)):
#             word = words[i]
#             for j in range(len(word)):
#                 if word[j] == searchWord[j]:
#                     if j == len(searchWord) - 1:
#                         return i + 1
#                 else:
#                     break

#         return -1
