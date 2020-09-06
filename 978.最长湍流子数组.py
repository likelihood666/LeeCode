#首先我们发现湍流子数组有两种可能存在的情况，因此我们要设置两个动态数组
#分别存储两种不同的湍流子数组的最长个数
#动态方程为只要满足条件，子数组的长度加一
def maxTurbulenceSize(A):
    n = len(A)
    if n == 0:
        return 0
    dp1 = [1] * n
    dp2 = [1] * n
    for i in range(1, n):
        if i % 2 == 0:
            if A[i] > A[i - 1]:
                dp1[i] = dp1[i - 1] + 1
                #数组满足了dp1的情况，即dp2不满足，那么dp2的长度要重新计数
                #因此将当前dp2的状态初始化为1
                dp2[i] = 1
            if A[i] < A[i - 1]:
                dp2[i] = dp2[i - 1] + 1
                dp1[i] = 1
        if i % 2 == 1:
            if A[i] < A[i - 1]:
                dp1[i] = dp1[i - 1] + 1
                dp2[i] = 1
            if A[i] > A[i - 1]:
                dp2[i] = dp2[i - 1] + 1
                dp1[i] = 1
    return max(max(dp1), max(dp2))