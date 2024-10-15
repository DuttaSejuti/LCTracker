110010

class Solution:
    def minimumSteps(self, s: str) -> int:
        min_steps = 0
        one_count = 0
        for i in range(len(s)):
            if s[i] == '1':
                one_count += 1
            else:
                min_steps += one_count
                # one_count = 0
        return min_steps
