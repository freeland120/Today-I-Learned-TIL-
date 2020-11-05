
n = 3

arr = []

for _ in range(3):
    arr.append(int(input()))

data = str(arr[0] * arr[1] * arr[2])

for i in range(10):
    cnt = 0
    for j in range(len(data)):
        if i == int(data[j]):
            cnt += 1
        else:
            continue
    print(cnt)

    