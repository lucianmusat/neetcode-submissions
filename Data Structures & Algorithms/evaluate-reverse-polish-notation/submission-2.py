class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = ['+', '-', '*', '/']
        stack = []
        for c in tokens:
            if c in operands:
                right_operand = stack.pop()
                left_operand = stack.pop()
                c = int(eval(str(left_operand) + c + str(right_operand)))
            stack.append(c)
        return int(stack.pop())