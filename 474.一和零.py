#主要是找到状态方程，
#1 + dp[i - item_0][j - item_1]的含义是，如果当下我选择把此次的字符串装在背包里，
#那么背包已装容量加1，并且去除此次字符串所占用的容量后，背包装下了之前多少个字符串，其值显示为
#dp[i - item_0][j - item_1]的值
def findMaxForm( strs, m, n):
    dp = [[0] * (n + 1) for i in range(m + 1)]
    for item in strs:
        item_0 = item.count("0")
        item_1 = item.count("1")
        for i in range(m, item_0 - 1, -1):
            for j in range(n, item_1 - 1, -1):
                dp[i][j] = max(dp[i][j], 1 + dp[i - item_0][j - item_1])
    return dp[m][n]