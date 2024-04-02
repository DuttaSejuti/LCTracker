class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        new_dict = dict()

        if len(set(s)) != len(set(t)): # no of unique characters should be same 
            return False

        for i in range(len(s)):
            if s[i] not in new_dict:
                new_dict[s[i]] = t[i]
            else:
                if new_dict[s[i]] != t[i]:
                    return False
        
        return True

    # def isIsomorphic(self, s: str, t: str) -> bool:
    #     s_dict = dict()
    #     t_dict = dict()

    #     converted_s = ''
    #     converted_t = ''

    #     for i in s:
    #         if i not in s_dict:
    #             # mapping each character to a distinct number
    #             s_dict[i] = len(s_dict) + 1

    #         converted_s += str(s_dict[i])
        
    #     for j in t:
    #         if j not in t_dict:
    #             t_dict[j] = len(t_dict) + 1

    #         converted_t += str(t_dict[j])
        
    #     if converted_s == converted_t:
    #         return True
        
    #     return False
