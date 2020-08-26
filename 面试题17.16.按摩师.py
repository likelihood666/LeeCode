class Solution:
    def massage(self, nums):
        #先获取数组的长度
        n = len(nums)
        #初始化状态数组,为了计算方便，将状态数组的dp[0]和dp[1]均设置为0
        dp = [0]*(n+2)
        #初始化最佳预约预约集合
        ans = 0
        #dp[0]和dp[1]只是为了计算方便，所以循环从2开始
        for i in range(2, n+2):
            #状态数组的当前值等于上一次状态值与上上次状态值加上当前状态值和中的最大值
            dp[i] = max(dp[i-1], dp[i-2]+nums[i-2])
            #利用ans接受状态数组的最大值
            ans = max(ans, dp[i])
        return ans
    

