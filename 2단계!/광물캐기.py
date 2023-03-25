'''
1. 다이아몬드 곡괭이가 최고임 (무조건 먼저 사용한다.)
2. 5개씩 끊어서 확인할 때 최소값인 것을 확인한다. (5개씩 끊어서 리스트에 저장한다.)
3. 다이아몬드 / 철 내림차순으로 정렬 (돌은 동일하므로 상관 없다.)
4. 다이아몬드 곡괭이부터 사용

헷갈렸던 곳
1. 그래프를 보면 바로 그리디 문제라는 것을 알았어야했으나 Backtraking으로 풀려다 1시간 날림
2. 앞으로 문제를 읽을 때 좀 더 정확하게 읽어야함
3. 곡괭이가 쓸 수 있을 때까지만 광물을 집어넣어야함. => 이후의 것들은 무조건 캘 수 없기에 sort에 포함되어 들어가면 안된다.

회고
1. 문제를 좀 더 천천히 똑바로 읽자
2. 서순 부분을 조심해서 사용하자
3. 리스트 내에서 아예 사용할 수 없는 부분이 있는지를 정확하게 확인하자
'''

from itertools import permutations
def solution(picks, minerals):
    graph = [(1,1,1),(5,1,1),(25,5,1)]
    stresses = []
    count = 0
    for i in range(0, len(minerals), 5):
        if count == sum(picks): 
            break
        else:
            count += 1
            l = minerals[i:i+5]
            stresses.append(l)
    stresses.sort(key = lambda x: (-x.count('diamond'), -x.count('iron'))) # 아예 캘 수 없는 광물들은 넣어놓아서는 안된다.
    result = 0
    for i in range(3):
        pick = picks[i] # 다이아 > 철 > 돌 곡괭이 순서대로 사용한다.

        while pick:
            if not stresses:
                return result
            pick -= 1
            stress = stresses.pop(0)
            for value in stress:
                if value == "diamond":
                    result += graph[i][0]
                elif value == "iron":
                    result += graph[i][1]
                elif value == "stone":
                    result += graph[i][2]
    return result