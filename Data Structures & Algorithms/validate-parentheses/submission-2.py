class Solution:
    def isValid(self, s: str) -> bool:
        correspondent = {
            '(': ')',
            '{': '}',
            '[': ']',
        }
        stack = []
        for c in s:
            # Add to the stack if opening brackets
            if c in correspondent.keys():
                stack.append(c)
            else:
                # Pop from the stack if closing brackets
                if not stack or correspondent[stack.pop()] != c:
                    return False
        # Check if we still have unmatched chars
        return not stack