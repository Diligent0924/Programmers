# 임의로 찍는 수에서 최대값을 구하는 방식 => 모든 노드를 확인한 뒤에 나타내야 할 것으로 보인다.
def solution(cards):
    N = len(cards)
    visited = [0] * N
    value = []
    # 그냥 연결되어 있는 경우의 수만 찾아서 넣는다.
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            count = 1
            now = cards[i] - 1
            while True:
                if visited[now]:
                    break
                else:
                    count += 1
                    visited[now] = 1
                    now = cards[now] - 1
        value.append(count)
    value.sort()
    print(calue)
    s1 = value.pop()
    s2 = value.pop()
    print(value)
    return s1 * s2