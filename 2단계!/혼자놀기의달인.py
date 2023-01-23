'''
해당 문제는 s1 / s2 2개만 구하는 문제였으며 노드도 정확하게 정해져 있었다.
하지만 나의 경우에는 이러한 문제의 조건들을 제대로 읽지 않아서 1시간 10분이라는 시간이 걸리게 되었다.
앞으로 문제를 좀 더 정확하게 확인할 필요가 있다고 생각한다. + 항상 노트로 구현의 순서를 정해서 풀어야한다.
+ 예외처리 (한개만 있을 떄와 같은) 또한 미리 그냥 적어놓는다고 생각하면 마음이 편할 것 같다.
'''

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
    if len(value) == 1:
        return 0
    else:
        value.sort()
        s1 = value.pop()
        s2 = value.pop()
        return s1 * s2