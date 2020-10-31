
# #n자리 k진수 중복없이 만든는 방법(한 케이스내,중복없는 순열)

# arr = []
# visited = []
# cnt = 0

# n = 0

# def recur(cur):
#     cnt = 0
#     if cur == n:
#         cnt += 1
#         return

#     for i in range(n):
#         if visited[i]:
#             continue
    
#         visited[i] = True
#         arr.append(i)
#         recur(cur+1)
#         arr.pop()
#         visited[i] = False




# #n자리 k진수 중복없이 만든는 방법(한 케이스내,중복없는 순열)
# #n-Rook
# arr = []
# visited = []
# cnt = 0

# n = 0

# def recur(cur):
#     cnt = 0
#     if cur == n:
#         cnt += 1
#         return

#     for i in range(n):
#         if visited[i]:
#             continue
    
#         visited[i] = True
#         arr.append(i)
#         recur(cur+1)
#         arr.pop()
#         visited[i] = False


# #n자리 k진수 중복없이 만든는 방법(한 케이스내,중복없는 순열)
# #n-Queen

# def recur():
#     #가지치기(정답이 안될것 같으면 return을 해라 ,정답인지 아닌지 판단하는 부분이 가지치기라고 생각하면 된다.)
#     #기저
#     #재귀

# arr = []
# n = 0

# def recur(cur):
#     for i in range(cur-1):
#         if cur-1 - i == abs(arr[i] - arr[cur-1]):
#             return

#         if cur == n:
#             cnt += 1
#             return
#         for i in range(n):
#             if visited[i]:
#                 continue

#             visited[i] = True
#             arr.append(i)
#             recur(cur+1)
#             arr.pop()
#             visited[i] = False



#질문하는 방식
#1.내가 이런 로직으로 이런 시도를 했다(기대값)
#2.이렇게 잘 못 나오더라(경향,어떻게 잘 못 나오는지)
#3.이런게 틀린 것 같아서 시도를 해봤는데 결과가 어떻게 달라지더라(디버깅)

#로직
#경향
#디버깅






















# import math
# import time


# def isPrime(N):
#     for i in range(2,math.floor(math.sqrt(N))+1):
#         if N % i == 0:
#             return False

#     return True


# def countPrimes(N):
#     count = 0 

#     for i in range(2,N+1):
#         if isPrime(i):
#             count += 1
            
#     return count



# def countPrimes2(N):
#     sieve = [False,False] + [True] * (N-1)
#     primes = []
#     count2 = 0
#     for i in range(2,N+1):
#         primes.append(i)
    
#         for j in range(i * 2, N+1, i):
#             sieve[j] = False

#     #print(sieve)

#     for k in range(2,N+1):
#         if sieve[k]:
#             count2 += 1       

#     return count2



# N = int(input())

# # result = isPrime(N)

# # if result == True:
# #     print(N,"은 소수입니다❗❗❗")

# # else:
# #     print(N,"은 소수가 아닙니다❗❗❗")


# countPrimes_time_start = time.time()
# result2 = countPrimes(N)
# countPrimes_elapsed = time.time() - countPrimes_time_start
# print(N,"까지의 소수의 갯수는:",result2,"개 입니다.")
# print(countPrimes_elapsed, '초')
# print(countPrimes_elapsed/60, '분')
# print(countPrimes_elapsed/60/60, '시간')



# countPrimes2_time_start = time.time()
# result3 = countPrimes2(N)
# countPrimes2_elapsed = time.time() - countPrimes2_time_start
# print(N,"까지의 소수는:",result3,"개 입니다.")
# print(countPrimes2_elapsed, '초')
# print(countPrimes2_elapsed/60, '분')
# print(countPrimes2_elapsed/60/60, '시간')


# from itertools import combinations

# N,M = map(int,input().split())

# data = []

# for i in range(1,N+1):
#     data.append(i)

# result = combinations(data,M)

# print('\n'.join(map(str,result)))




# def n_queens(i,col):
#     n = len(col) - 1
    
#     if promising(i,col):
#         if i == n:         
#             print(col[1:n+1])
#         else:
#             for j in range(1,n+1):
#                 col[i+1] = j
#                 n_queens(i+1,col)
        


# def promising(i,col):
#     k = 1
#     flag = True

#     while k<i and flag:
#         if col[i] == col[k] or abs(col[i]-col[k]) == (i - k):
#             flag = False
#         k += 1
#     return flag



# N = int(input())

# col = [0]*(N+1)

# n_queens(0,col)



# cnt = 0
# def recur(depth):

#     global cnt
#     if depth == n:
#         cnt += 1
#         return

#     for i in range(n):
#         if visited[i] or visited2[depth+i] or visited3[depth-i]:
#             continue

#         visited3[depth-i] = True
#         visited2[depth+i] = True
#         visited[i]=True
#         arr.append(i)
#         recur(depth+1)
#         arr.pop()
#         visited[i] = False
#         visited2[depth+i] = False
#         visited3[depth-i] = False
# n = int(input())

# arr = []



# visited = [0] * 20
# visited2 = [0] * 50
# visited3 = [0] * 100

# recur(0)
# print(cnt)









# cnt = 0

# def n_queen(depth):
#     global cnt
#     if depth == N:
#         cnt += 1
#         return

#     for i in range(N):
#         if col[i] or col2[depth+i] or col3[depth-i]:
#             continue
        
#         col3[depth-i] = True
#         col2[depth+i] = True
#         col[i] = True
        
#         n_queen(depth+1)
        
#         col[i] = False
#         col2[depth+i] = False
#         col3[depth-i] = False

# N = int(input())



# col = [0] * 20
# col2 = [0] * 50
# col3 = [0] * 50

# n_queen(0)
# print(cnt)

