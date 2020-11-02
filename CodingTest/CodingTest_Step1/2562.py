n = 9
cnt = 0
arr = []
while True:
    if cnt == n:
        break

    data = int(input())
    arr.append(data)
    cnt += 1

result1 = max(arr)
result2 = arr.index(result1)+1

print(result1)
print(result2)