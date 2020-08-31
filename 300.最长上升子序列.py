def lengthOfLIS(nums):
    n = len(nums)
    #首先排除空列表的情况
    if n == 0:
        return 0
    #创建状态数组
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                #dp[j] + 1的含义在于，它将所有在第i个数前面且比其小的数计下
                #并且第i个状态dp[i]累计了在其前面且比其小的的数的个数
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp[0:])
