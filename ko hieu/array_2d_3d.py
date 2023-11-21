






M = [[0,1,1,0],
     [0,1,1,0],
     [0,0,0,1]
     ]

# Output: 3



def arr(M):
    row = len(M)
    col = len(M[0])

    ans = 0 

    # dp[i][j][0] > horizontal
    # dp[i][j][1] > vertical
    # dp[i][j][2] > diagonal
    # dp[i][j][3] > anti diagonal


                    #               4       x           3
    dp = [[[0] * 4 for j in range(col)] for _ in range(row)]


    #len(dp) = 3 

    for i in range(row): # 0 1 2 
        for j in range(col): # 0 1 2 3 
            if M[i][j] == 1:
                dp[i][j][0] = dp[i][j - 1][0] + 1 if j > 0 else 1 
                dp[i][j][1] = dp[i - 1][j][1] + 1 if i > 0 else 1 
                dp[i][j][2] = dp[i - 1][j - 1][2] + 1 if i > 0 and j > 0 else 1 
                dp[i][j][3] = dp[i - 1][j + 1][3] + 1 if i > 0 and j < col - 1 else 1 
                ans = max(ans, max(dp[i][j]))
    return ans

# O(mn)
# 0(mn)

print(arr(M))


