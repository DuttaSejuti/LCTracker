class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        i, l = 0, len(s)
        if l != len(goal): return False
        if set(s) != set(goal): return False
        s = deque(s)
        goal = deque(goal)

        while i < l:
            left_char = s.popleft()
            s.append(left_char)
            if s == goal:
                return True
            i += 1
        return False

# class Solution:
#     def rotateString(self, s: str, goal: str) -> bool:
#         l = len(s)
#         if l != len(goal): return False
#         concat_sting = s + s # this creates a string that contains all possible rotations of s

#         return concat_string.find(goal) != -1 # similar to checking (goal in s + s)
