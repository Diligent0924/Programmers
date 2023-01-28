def solution(maps):
    result = [] # 결과값
    def bfs(first_i,first_j):
        count = graph[first_i][first_j]
        graph[first_i][first_j] = "X"
        queue = [(first_i, first_j)]
        while queue:
            i, j = queue.pop(0)
            for di, dj in (0,1),(0,-1),(-1,0),(1,0):
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < M and graph[ni][nj] != "X":
                    count += graph[ni][nj]
                    queue.append((ni,nj))
                    graph[ni][nj] = "X"
        return count
    
    N, M = len(maps), len(maps[0])
    graph = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if maps[i][j] == "X":
                graph[i][j] = maps[i][j]
            else:
                graph[i][j] = int(maps[i][j])
    print(graph)
    for i in range(N):
        for j in range(M):
            if graph[i][j] != "X":
                result.append(bfs(i,j))
    if result:
        return sorted(result)
    else:
        return [-1]