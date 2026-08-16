from collections import deque

class Solution:
    def checkValidString(self, s: str) -> bool:
        left_p = deque()
        stars = deque()

        for i, c in enumerate(s):
            if c == '(':
                left_p.append(i)
            elif c == '*':
                stars.append(i)
            elif c == ')':
                if left_p:
                    left_p.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
        
        while left_p and stars:
            if left_p[-1] < stars[-1]:
                left_p.pop()
                stars.pop()
            else:
                return False
        
        return not left_p
                