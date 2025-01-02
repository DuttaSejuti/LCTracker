class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        ans = [] #[0]*len(queries)
        count = 0
        prefixCount = [0]*len(words)
        vowels = ['a', 'e', 'i', 'o', 'u']
        
        # pre compute
        for i in range(len(words)):
            if words[i][0] in vowels and words[i][-1] in vowels:
                count += 1
            prefixCount[i] = count
        
        for i in range(len(queries)):
            start, end = queries[i][0], queries[i][1]
            wordTillEnd = prefixCount[end]
            wordTillStart = 0 if start == 0 else prefixCount[start-1]
            wordFound = wordTillEnd - wordTillStart
            ans.append(wordFound)

        return ans
