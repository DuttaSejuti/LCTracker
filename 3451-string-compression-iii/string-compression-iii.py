# class Solution:
#     def compressedString(self, word: str) -> str:
#         i = 0
#         result  = []

#         while i < len(word):
#             count = 1 # Start counting the current character
#             curr = word[i]

#              # Count up to 9 consecutive characters
#             while i + 1 < len(word) and word[i+1] == curr and count < 9:
#                 count += 1
#                 i += 1
            
#             result.append(str(count) + curr) 
#             i += 1 # Move to the next character group

#         return ''.join(result)
    
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

class Solution:
    def compressedString(self, word: str) -> str:
        result = []
        count = 1  # Start with a count of 1 for the first character
        
        for i in range(1, len(word)):
            # If the current character is the same as the previous one, increase the count
            if word[i] == word[i - 1]:
                count += 1
                # If count reaches 9, append it and reset the count
                if count > 9:
                    result.append("9" + word[i - 1])
                    count = 1
            else:
                result.append(str(count) + word[i - 1])
                count = 1
        
        # Append the last character group with count, ensuring it's capped at 9
        result.append(str(count))
        result.append(word[-1])
        
        return ''.join(result)
