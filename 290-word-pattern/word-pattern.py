class Solution:
    # pattern = "abba", s = "dog cat cat dog"
    def wordPattern(self, pattern: str, s: str) -> bool:
        match = list(s.split(' ')) #['dog', 'cat', 'cat', 'dog']
        new_dict = dict() #{}

        if len(match) != len(pattern) or len(set(match)) != len(set(pattern)):
            return False
        for i in range(len(match)):
            if new_dict.get(pattern[i]) == None:
                new_dict[pattern[i]] = match[i]
            else:
                if new_dict.get(pattern[i]) != match[i]:
                    return False
        return True