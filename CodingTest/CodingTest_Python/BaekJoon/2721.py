#삼각수의 합
# n(n+1)/2


def Tri_Sum(n):
    return n * (n+1) // 2




T = int(input())


for i in range(T):
    sum = 0
    n = int(input())

    for j in range(1,n+1):
        sum += Tri_Sum(j+1) * j
    print(sum)