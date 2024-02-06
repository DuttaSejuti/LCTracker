class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = list()
        new_dict = dict()

        for i in range(len(strs)):
            temp = "".join(sorted(strs[i]))
            if temp not in new_dict:
                new_dict[temp] = [strs[i]]
            else:
                new_dict[temp].append(strs[i])
        
        for v in new_dict.values():
            result.append(v)
        return result