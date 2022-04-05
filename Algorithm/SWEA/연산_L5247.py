import sys
from collections import deque

sys.stdin = open('input.txt')

def bfs(N, M):
    visited = [False] * (M + 11)
    queue = deque()
    queue.append((N, 0))
    while queue:
        number, cnt = queue.popleft()
        if number == M:
            return cnt
        else:
            d_number = [1, -1, number, -10]
            for i in range(4):
                new_number = number + d_number[i]
                if 1 <= new_number <= M + 10 and visited[new_number] == False:
                    queue.append((new_number, cnt + 1))
                    visited[new_number] = True

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    answer = bfs(N, M)

    print(f'#{tc} {answer}')