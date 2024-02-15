class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #TC: O(n), SC: O(n)
        if len(s) != len(t):
            return False

        char_count = {}

        # Increment frequency for characters in string s
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        # Decrement frequency for characters in string t
        for char in t:
            if char not in char_count:
                return False
            char_count[char] -= 1
            if char_count[char] == 0:
                del char_count[char]

        # If the dictionary is empty, the strings are anagrams
        print(char_count)
        return not bool(char_count)


        #TC: O(S+T), SC: O(S+T)
        #one-liner, will not be accepted in interview
        # return Counter(s) == Counter(t)

        # if len(s) != len(t):
        #     return False

        # countS, countT = {}, {}
        # for i in range(len(s)): #taking s, becuse both are have to be same length
        #     countS[s[i]] = countS.get(s[i], 0) + 1
        #     countT[t[i]] = countT.get(t[i], 0) + 1

        # for c in countS:
        #     #using get, because key of countS, may not be present on countT, to prevent KeyError
        #     if countS[c] != countT.get(c, 0):
        #         return False
        # return True

        # TC: O(nlogn)
        # if sorted(s) == sorted(t):
        #     return True
        # else:
        #     return False

        
        