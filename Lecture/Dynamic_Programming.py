"""Dynamic Programming"""

# Writing a recursive algorithm for computing the nth Fibonacci number


def fib(input_num) -> int:
    if input_num == 0:
        return 0
    if input_num == 1:
        return 1
    return fib(input_num - 1) + fib(input_num - 2)


# Writing a dynamic programming algorithm for Long Common Subsequence(LCS)
'''
Application: Comparison of two DNA Strings
Brute Force: Comparing each subsequences of two strings -> O(2^m),
'm' being the length of the shorter string
Dynamic Programming: O(m*n) or O(n^2), because c[i,j] is calculated in constant time, 
and there are m * n elements in the array
'''

def LCS_Length(string1, string2, m, n):
    L = []
    for i in range(m + 1):
        L.append([0] * (n + 1))

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif string1[i - 1] == string2[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    return L[m][n]


# Writing a dynamic programming algorithm for O-1 Knapsack Problem
'''
Application: Packing a knapsack with the maximum value
'''
def Knapsack_O1(W, wt, value, n):
    K = []
    for i in range(n + 1):
        L = []
        for x in range(W + 1):
            L.append(x)
        K.append(L)

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(value[i - 1] + K[i - 1]
                              [w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    return K[n][W]
