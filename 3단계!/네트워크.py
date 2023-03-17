def network(now, visited, n, computers):
    for i in range(n):
        if not visited[i] and computers[now][i] == 1:
            visited[i] = 1
            network(i, visited, n, computers)

def solution(n, computers):
    result = 0 # 몇 개의 네트워크가 있는지 확인하는 답안
    visited = [0] * n # 갔었던 node를 확인하기 위하여 설정한다.
    for i in range(n):
        if not visited[i]: # 방문하지 않았던 곳이면 시작한다.
            result += 1
            visited[i] = 1
            network(i, visited, n, computers)
    return result