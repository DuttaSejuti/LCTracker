class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = dict()
        t_dict = dict()

        converted_s = ''
        converted_t = ''

        for i in s:
            if i not in s_dict:
                # mapping each character to a distinct number
                s_dict[i] = len(s_dict) + 1

            converted_s += str(s_dict[i])
        
        for j in t:
            if j not in t_dict:
                t_dict[j] = len(t_dict) + 1

            converted_t += str(t_dict[j])
        
        if converted_s == converted_t:
            return True
        
        return False

        # s_dict = dict()
        # t_dict = dict()
        
        # for i in s:
        #     s_dict[i] = s_dict.get(i, 0) + 1
        
        # for j in t:
        #     t_dict[j] = t_dict.get(j, 0) + 1
        
        # if len(s_dict) != len(t_dict):
        #     return False
        
        # if list(s_dict.values()) != list(t_dict.values()):
        #     return False

        # return True
