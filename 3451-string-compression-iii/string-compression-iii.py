class Solution:
    def compressedString(self, word: str) -> str:
        result = []
        count = 1

        for i in range(len(word)-1):
            if word[i] == word[i+1]:
                count += 1
                if count > 9:
                    result.append(str(count-1))
                    result.append(word[i])
                    count = 1
            else:
                result.append(str(count))
                result.append(word[i])  
                count = 1
        result.append(str(count))
        result.append(word[-1])
            
        return ''.join(result)

