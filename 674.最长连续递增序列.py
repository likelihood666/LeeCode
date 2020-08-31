def findLengthOfLCIS(nums):
    n = len(nums)
    #设置状态数组
    dp = [1] * n
    #首先排除空数组和只有一个数的数组
    if n == 0:
        return 0
    if n == 1:
        return 1
    for i in range(1, n):
        if nums[i] > nums[i - 1]:
            #使用状态数组中的第i个数dp[i]将数组中在其前面且比其小的数的
            #个数记录下来。如果不满足递增的关系，则当前记录的数为初始化的1
            #即递增数组从头计数
            dp[i] = dp[i - 1] + 1
    return max(dp)