class Solution {
    private int fib(int n) {
        if (n == 0) return 0;
        if (n == 1) return 1;
        
        // Binet's formula
        final double sqrt_5 = Math.sqrt(5);
        final double numerator = Math.pow(1 + sqrt_5, n) - Math.pow(1 - sqrt_5, n);
        final double denominator = Math.pow(2, n) * sqrt_5;

        return (int) Math.round(numerator / denominator);
    }

    public int climbStairs(int n) {
        return fib(n + 1);
    }
}
