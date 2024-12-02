class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(' ')

        for i in range(len(words)):
            word = words[i]
            for j in range(len(word)):
                if word[j] == searchWord[j]:
                    if j == len(searchWord) - 1:
                        return i + 1
                else:
                    break

        return -1
