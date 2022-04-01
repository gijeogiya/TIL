def Binary_Search(key, left, right):
    cnt = 0
    while True:
        center = (left + right) // 2
        if key > center:
            left = center
        elif key < center:
            right = center
        else:
            break
        cnt += 1
    return cnt

T = int(input())

for tc in range(1, T+1):
    cnt = 0
    N, M = map(int, input())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
