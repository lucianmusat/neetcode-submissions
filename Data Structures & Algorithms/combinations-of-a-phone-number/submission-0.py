class Solution:
    digit_map = {
        '2': ["a", "b", "c"],
        '3': ["d", "e", "f"],
        '4': ["g", "h", "i"],
        '5': ["j", "k", "l"],
        '6': ["m", "n", "o"],
        '7': ["p", "q", "r", "s"],
        '8': ["t", "u", "v"],
        '9': ["w", "x", "y", "z"],
    }

    def letterCombinations(self, digits: str) -> List[str]:
        
        def backtrack(i: int, cur_combination: str) -> None:
            # print(f"i: {i}, current combination: {cur_combination}")
            if i == len(digits) and len(cur_combination) == len(digits) and cur_combination != "":
                result.append(cur_combination)
                return
            
            for start in range(i, len(digits)):
                for letter in self.digit_map[digits[start]]:
                    cur_combination += letter
                    backtrack(start + 1, cur_combination)
                    cur_combination = cur_combination[:-1]
        

        result = []
        backtrack(0, "")
        return result