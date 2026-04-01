def highest_val_subseq(a,b,vals):
    len_a, len_b = len(a), len(b)

    dp = [[0] * (len_a + 1) for i in range(len_b + 1)]
    # print(dp)

    
    #i -> b, j -> a
    for i in range(1, len_b + 1):
        # print(dp)
        for j in range(1, len_a + 1):
            if a[j-1] == b[i-1]:
                dp[i][j] = dp[i-1][j-1] + vals[a[j-1]]
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    # print(dp[-1][-1])
    # print(dp)

    j = len_a
    i = len_b

    result = []

    while i > 0 and j > 0:
        # print("\n\nNEW ITERATION")
        # print(f"i: {i}, j: {j}, {dp[i][j]}")
        if a[j-1] == b[i-1]:
            # print(f" Appending...{a[j-1]} == {b[j-1]} from {(i,j)} with value {dp[i][j]}")
            result.append(a[j-1])
            i -= 1
            j -= 1
        else:
            # print(f"up: {dp[i-1][j]}, left: {dp[i][j-1]}")
            if dp[i-1][j] > dp[i][j-1]:
                i -= 1
            elif dp[i][j-1] > dp[i-1][j]:
                j -=1
           

    return (dp[-1][-1], "".join(result[::-1]))

# if mai
# print(highest_val_subseq("aacb", "caab", {'c':5, 'a':2, 'b':4}))