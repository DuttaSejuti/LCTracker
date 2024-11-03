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
# bcdea