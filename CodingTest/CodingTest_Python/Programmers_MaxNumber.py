## 정렬 "가장 큰 수"

def solution(numbers):
    

    numbers = list(map(str,numbers))
    numbers.sort(key = lambda x : x*3, reverse=True)
    
    return str(int(''.join(numbers)))


list1 = [6,10,2]


    
print(solution(list1))



