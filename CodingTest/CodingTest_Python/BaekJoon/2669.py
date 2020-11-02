#완전탐색으로 풀이 가능?
#수식으로 풀이 가능?

#2차원 배열 이용하기 [[0]*101 for _ in range(101)]
#사각형 부분만 1로 바꿔서 sum을 통해 답을 구해보자
arr = [[0] * 101 for _ in range(101)]

for _ in range(4):
    x1,y1,x2,y2 = map(int,input().split(" "))

    for i in range(x1,x2):
        for j in range(y1,y2):
            arr[i][j] = 1

ans = 0
for row in arr:
    ans += sum(row)
print(ans)
