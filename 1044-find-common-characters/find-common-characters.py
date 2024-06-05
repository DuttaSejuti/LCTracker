class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        new_dict_1 = dict()
        new_dict_2 = dict()
        result = list()

        for w in words[0]:
            new_dict_1[w] = new_dict_1.get(w, 0) + 1

        for i in range(1, len(words)):
            for w in words[i]:
                new_dict_2[w] = new_dict_2.get(w, 0) + 1
            for k in new_dict_1:
                new_dict_1[k] = min(new_dict_2.get(k, 0), new_dict_1.get(k, 0))
            new_dict_2 = dict()

        for k in new_dict_1:
            for i in range(new_dict_1[k]):
                result.append(k)

        return result
             