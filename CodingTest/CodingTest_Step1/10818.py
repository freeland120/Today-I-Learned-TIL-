import sys
n = int(input())

arr = list(map(int,sys.stdin.readline().split()))
ret1 = min(arr)
ret2 = max(arr)

print(ret1,ret2)