# using recursion
def recursive(p, i, j):
    if i == j:
        return 0
    minops = 10**9
    for k in range(i, j):
        minops = min(minops, recursive(p, i, k) + recursive(p, k+1, j) + p[i-1]*p[k]*p[j])
    return minops

def dp_bottom_up(p):
    n = len(p)
    # let dp[i][j] be the minimum number of operations for multiplytin Ai... Aj
    # We want dp[1][n-1]
    dp = [[0]*n for _ in range(n)]

    for l in range(2, n):
        for i in range(1, n - l + 1):
            j = i + l - 1
            dp[i][j] = 10**9
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + p[i-1]*p[k]*p[j])
                
    return dp[1][n-1]



arr = [1, 2, 3, 4, 3] 
n = len(arr)
print(recursive(arr, 1, n-1))

print(dp_bottom_up(arr))
# print(MatrixChainOrder(arr))

