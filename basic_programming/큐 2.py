from collections import deque
import sys

N = int(input())

queue = deque()
num = 0

for i in range(N):
    order = sys.stdin.readline().rstrip().split()
    # print(order)
    if order[0] == 'push':
        queue.append(order[1])
        num += 1
    else:
        if order[0] == 'pop':
            if num == 0:
                print(-1)
            else:
                print(queue.popleft())
                num -= 1
        elif order[0] == 'size':
            print(num)
        elif order[0] == 'empty':
            if num == 0:
                print(1)
            else:
                print(0)
        elif order[0] == 'front':
            if num == 0:
                print(-1)
            else:
                print(queue[0])
        elif order[0] == 'back':
            if num == 0:
                print(-1)
            else:
                print(queue[len(queue) - 1])
