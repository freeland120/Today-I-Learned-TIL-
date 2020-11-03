

N = int(input())
S = input()

if S.count("LL") > 0:
    print(len(S.replace("LL","S"))+1)

else:
    print(N)