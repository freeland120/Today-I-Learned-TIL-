import sys
n = int(input())

result = []
arr = list(map(int,sys.stdin.readline().split()))


target = max(arr)


for i in range(len(arr)):
    result.append(arr[i]/target*100)

print(sum(result)/n)