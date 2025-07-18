class Solution:
    def possibleStringCount(self, word: str) -> int:
        new_dict = dict()
        prev = word[0]
        for i in range(1, len(word)):
            if prev == word[i]: # keeping track of the consequtive char
                if new_dict.get(word[i], 0) == 0:
                    new_dict[word[i]] = 2
                else:
                    new_dict[word[i]] = new_dict.get(word[i], 0) + 1   
            prev = word[i]
        
        # if prev == word[-1]:
        #     new_dict[word[-1]] = new_dict.get(word[-1], 0) + 1
        
        print(new_dict)
        total_count = 1 # the original string itself can be an intended string
        for k in new_dict.keys():
            if new_dict[k] > 1:
                total_count += new_dict[k] - 1
        return total_count
