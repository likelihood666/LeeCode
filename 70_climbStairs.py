class Solution:
    def climbStairs(self, n):
        """
        n=1时，有1种方法
        n=2时，有2种方法
        n=3时，有3种方法
        n=4时，有5种方法
        发现第n个台阶的方法数是前两个台阶方法的总和
        """
        fir = 1 #设定n=1的初始值
        sed = 2 #设定n=2的初始值
        Total = 0 #设定方法总数的初始值
        for i in range(2, n):
            Total = fir + sed
            fir = sed
            sed = Total
        # 取max是因为在n=1，2时，Total为0
        return max(Total, n)