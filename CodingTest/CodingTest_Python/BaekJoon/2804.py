
a,b = map(str,input().split())

R = 0
C = 0

for i in range(len(a)):
    idx = b.find(a[i])

    if idx >= 0:
        R = idx
        C = i
        break

for i in range(len(b)):
    for j in range(len(a)):
        if i == R:
            print(a,end="")
            break
        elif j == C:
            print(b[i],end="")
        else:
            print('.',end="")   
    print()