def fishing(row, col):
    fishs = 0
    for d_row in range(K):
        for d_col in range(K):
            fishs += matrix[row + d_row][col + d_col]
    for d_row in range(1, K - 1):
        for d_col in range(1, K - 1):
            fishs -= matrix[row + d_row][col + d_col]
    return fishs

T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for row in range(N - K + 1):
        for col in range(M - K + 1):
            result = max(result, fishing(row, col))

    print(f'#{tc} {result}')