



def highest_val_subseq(a,b,vals):
    len_a, len_b = len(a), len(b)

    dp = [[0] * (len_a + 1)] * (len_b + 1)
    
    #i -> b, j -> a
    for i in range(1, len_b + 1):
        # print(dp)
        for j in range(1, len_a + 1):
            if a[j-1] == b[i-1]:
                dp[i][j] = dp[i-1][j-1] + vals[a[j-1]]
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    print(dp[-1][-1])



highest_val_subseq("aacb", "caab", {'c':5, 'a':2, 'b':4})