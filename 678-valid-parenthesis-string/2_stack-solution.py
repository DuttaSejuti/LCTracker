class Solution:
# TC: O(n), SC:O(n)
    def checkValidString(self, s: str) -> bool:
      open_brackets = list()
      stars = list()

      for i in range(len(s)):
        if s[i] == '(':
          open_brackets.append(i)
        elif s[i] == '*':
          stars.append(i)
        # s[i] == ')'
        else:
          if open_brackets: # if open_brackets has entry
            open_brackets.pop()
          elif stars:
            stars.pop()
          else:
            return False
        
      # check for remaining open_brackets and stars
        while open_brackets and stars:
          # if open bracket appears after a star, then it can not be balanced
          if open_brackets.pop() > stars.pop():
            return False

        # if open_brackets:
        #   return False
        # else:
        #   return True

        return not open_brackets # not False means True

          
