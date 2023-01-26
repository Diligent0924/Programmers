def solution(m, n, board):
    graph = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            graph[i][j] = board[i][j]
    
    result = 0
    while True:
        pong = []
        # 4분면 값을 확인한다.
        for i in range(m-1):
            for j in range(n-1):
                if graph[i][j] and graph[i][j] == graph[i][j+1] == graph[i+1][j] == graph[i+1][j+1]:
                    for di,dj in (0,1),(1,0),(0,0),(1,1):
                        ni, nj = i + di, j + dj
                        if (ni,nj) not in pong:
                            pong.append((ni,nj))
        if not pong:
            break
        else:
            result += len(pong)
            for i,j in pong:
                graph[i][j] = 0
            # 한칸씩 내려가야한다.
            for j in range(n): # 가로 기준으로 탐색
                for i in range(m-1,0,-1): # 세로 뒤에서부터 탐색
                    if not graph[i][j]: # 만약 0이라면
                        for h in range(i-1, -1,-1): 
                            if graph[h][j]:                            
                                graph[i][j], graph[h][j] = graph[h][j], graph[i][j]
                                break
        # print(graph)
                            

    return result