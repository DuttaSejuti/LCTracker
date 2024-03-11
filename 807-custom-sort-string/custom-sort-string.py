class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq_s = dict()
        result = ''

        # keeping the freq of each char in s; s can have duplicate char
        # which would append in the result string; order will have unique char only
        for char in s:
            freq_s[char] = freq_s.get(char, 0) + 1
        
        # iterating the order string, as we need to maintain the order of this string
        for char in order:
            if char in freq_s and freq_s.get(char):
                # if a char exists in order, the #of times it occur in the 
                # string s has to maintain order; char * freq
                result += char * freq_s.get(char)
                freq_s[char] = 0

        # to append the rest of the char of s in the result string
        for f in freq_s:
            if freq_s[f] > 0:
                result += freq_s[f] * f # as the order doesn't matter anymore
        
        return result
        