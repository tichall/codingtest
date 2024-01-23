# 28279번 덱 2
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
deq = deque()

for i in range(n) :
    order= list(map(int, input().strip().split()))
    if order[0] == 1 :
        deq.appendleft(order[1])
    elif order[0] == 2 :
        deq.append(order[1])
    elif order[0] == 3 :
        if deq : 
            print(deq.popleft())
        else :
            print(-1)
    elif order[0] == 4 :
        if deq :
            print(deq.pop())
        else :
            print(-1)
    elif order[0] == 5 :
        print(len(deq))
    elif order[0] == 6 :
        if deq :
            print(0)
        else :               
            print(1)
    elif order[0] == 7 :
        if deq :
            print(deq[0])
        else :
            print(-1)
    elif order[0] == 8 :
        if deq :
            print(deq[-1])
        else :
            print(-1)