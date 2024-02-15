class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # TC: O(m*n*26) = O(m*n), SC: O()
        new_dict = defaultdict(list) #default value is a list; charCountArray: [anaagrams]

        for word in strs:
            count = [0]*26
            for c in word:
                count[ord(c) - ord('a')] += 1
            new_dict[tuple(count)].append(word) #list can not be keys,so tuple
        return new_dict.values()

        # TC: O(m*nlogn) SC: O(n)
        # result = list()
        # new_dict = dict()

        # for i in range(len(strs)):
        #     temp = "".join(sorted(strs[i]))
        #     if temp not in new_dict:
        #         new_dict[temp] = [strs[i]]
        #     else:
        #         new_dict[temp].append(strs[i])
        
        # for v in new_dict.values():
        #     result.append(v)
        # return result