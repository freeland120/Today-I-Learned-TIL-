#달팽이는 하루에 a-b 만큼 이동


A,B,V = map(int,input().split())

tmp = 0

while True:
    
    if tmp == V:
        break
    
    tmp = A-B
    
    if tmp != V:
    
    