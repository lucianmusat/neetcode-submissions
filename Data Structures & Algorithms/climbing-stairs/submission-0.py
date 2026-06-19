class Solution:
    def climbStairs(self, n: int) -> int:
        def fib(n: int):
            if n == 0: return 0
            if n == 1: return 1
            # Binet's Fibonacci Number Formula
            sqrt_5 = math.sqrt(5)
            numerator = math.pow(1 + sqrt_5, n) - math.pow(1 - sqrt_5, n)
            denominator = math.pow(2, n) * sqrt_5
            return int(round(numerator / denominator))
        
        return fib(n + 1)