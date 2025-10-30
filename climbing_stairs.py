# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 st


class Solution(object):
    def climbStairs(self, n):
        if n <= 2:
            return n
        
        one, two = 2, 1   # base cases: f(2)=2, f(1)=1
        for i in range(3, n + 1):
            one, two = one + two, one  # f(n) = f(n-1) + f(n-2)
        
        return one
    
#  O(N)   TIME COMPLEXITY