n = int(input())

for _ in range(n):
    data = list(input())

    sum = 0
    cnt = 0

    for i in data:
        if i == 'O':
            cnt += 1
        elif i == 'X':
            cnt = 0
        else:
            continue
        sum += cnt
    print(sum)
