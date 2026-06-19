class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # Use the start:stop:step way to check if a string is equal
        # to it's reverse
        def is_palindrome(string: str) -> bool:
            return string == string[::-1]

        def backtrack(start: int, intermediary) -> None:
            # We reached the end of one tree branch
            if start == len(s):
                result.append(intermediary.copy())
                return
            
            # Check starting from start, 1 char, 2 chars, 3 chars etc.
            for end in range(start + 1, len(s) + 1):
                if is_palindrome(s[start:end]):
                    intermediary.append(s[start:end])
                    backtrack(end, intermediary)
                    intermediary.pop()
        
        result = []
        backtrack(0, [])
        return result