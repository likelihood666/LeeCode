def minCostClimbingStairs(cost):
    #题目表达的意思是最小花费来越过这个数组，实际上的楼梯顶是不存在的
    #我们添加一个楼梯顶，并设置花费为0
    #每次可以选择走一个楼梯或者两个楼梯，即走上第i个台阶的方法为前i-1次总花费加上当前花费
    #或者是前i-2次花费加上当前花费
    cost.append(0)#构造楼梯顶
    n = len(cost)
    dp = [0]*n
    dp[0] = cost[0]
    dp[1] = cost[1]
    for i in range(2, n):
        dp[i] = min(dp[i-1]+coat[i], dp[i-2]+cost[i])
    return dp[-1]