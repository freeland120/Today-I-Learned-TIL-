n = 10

arr = []
result = []
for _ in range(n):
    data = int(input()) % 42
    arr.append(data)

result = set(arr)

print(len(result))