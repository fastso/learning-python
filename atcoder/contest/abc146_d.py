n = int(input())
a = [list(map(int, input().split())) for i in range(n-1)]

dp_count = [0]*n
for i in range(n-1):
    dp_count[a[i][0]-1] += 1
    dp_count[a[i][1]-1] += 1

print(dp_count)

# dp = [0] * n
# dp_matrix = [[0]*n for i in range(n)]
#
#
# dp[a - 1] = 1
# dp[b - 1] = 1
# dp_matrix[a - 1][0] = 1
# dp_matrix[b - 1][0] = 1
# max_color = 1
#
# ans = list()
# ans.append(1)
# for i in range(1, n - 1):
#     a, b = map(int, input().split())
#     dp[a - 1] += 1
#     dp[b - 1] += 1
#     max_color = max(max_color, max(dp[a - 1], dp[b - 1]))
#     for j in range(max_color):
#         if dp_matrix[a - 1][j] == 0 and dp_matrix[b - 1][j] == 0:
#             dp_matrix[a - 1][j] = 1
#             dp_matrix[b - 1][j] = 1
#             ans.append(j+1)
#             break

# print(max(ans))
# for i in range(n - 1):
#     print(ans[i])
