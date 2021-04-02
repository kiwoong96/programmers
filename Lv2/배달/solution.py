def solution(N, road, K):
    answer = 0

    graph = [[1e9 for _ in range(N + 1)] for _ in range(N + 1)]

    for now in road:
        start, end, distance = now[0], now[1], now[2]
        graph[start][end] = min(graph[start][end], distance)
        graph[end][start] = min(graph[end][start], distance)

    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if i == j:
                    graph[i][j] = 1
                    continue
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    for i in range(1, N + 1):
        if graph[1][i] <= K:
            answer += 1
    return answer