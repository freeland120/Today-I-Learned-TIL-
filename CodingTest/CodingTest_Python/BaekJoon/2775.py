# ex) 3층 3호에 살려고 하면 2층 1호, 2층 2호, 2층 3호에
# 사는 사람들의 합만큼 3층 3호에 데리고 살아야 함
# 3층 2호에 산다면 2층 1호, 2층 2호에 사는 사람들의 합
# 그렇다면 3층 3호에 데리고 사는 사람은 3층 2호 + 2층 3호


T = int(input())

for _ in range(T):
    a = int(input())
    b = int(input())

    sum_people = [i for i in range(1,b+1)]

    for _ in range(a):
        for j in range(1,b):
            sum_people[j] += sum_people[j-1] 
        
    print(sum_people[-1])