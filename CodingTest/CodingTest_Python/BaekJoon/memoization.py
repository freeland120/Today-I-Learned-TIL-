
dp = [-1] * 100000

def fibo(n):

    if dp[n] != -1:
        return dp[n]

    if n<=1:
        return n
    
    else:
        dp[n] = fibo(n-1) + fibo(n-2)
        return dp[n]



#f(n) = not ( f(n-1) and f(n-2) and f(n-3))