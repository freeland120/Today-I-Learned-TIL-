T = int(input())

for _ in range(T):
    avg = 0

    arr = list(map(int,input().split()))

    avg = sum(arr[1:]) // arr[0]

    cnt = 0
    for i in range(1,len(arr)):
        if avg < arr[i]:
            cnt += 1
        else:
            continue
    
    ratio = (cnt / arr[0]) * 100
    print("%.3f%%" %ratio)