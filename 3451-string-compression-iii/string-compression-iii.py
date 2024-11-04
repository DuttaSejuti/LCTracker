class Solution:
    def compressedString(self, word: str) -> str:
        i = 0
        result  = []

        while i < len(word):
            count = 1 # Start counting the current character
            curr = word[i]

             # Count up to 9 consecutive characters
            while i + 1 < len(word) and word[i+1] == curr and count < 9:
                count += 1
                i += 1
            
            result.append(str(count) + curr) 
            i += 1 # Move to the next character group

        return ''.join(result)
    
# class Solution:
#     def compressedString(self, word: str) -> str:
#         result = []
#         count = 1

#         for i in range(len(word)-1):
#             if word[i] == word[i+1]:
#                 count += 1
#                 if count > 9:
#                     result.append(str(count-1))
#                     result.append(word[i])
#                     count = 1
#             else:
#                 result.append(str(count))
#                 result.append(word[i])  
#                 count = 1
#         result.append(str(count))
#         result.append(word[-1])
            
#         return ''.join(result)
