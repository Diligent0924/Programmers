'''
점을 찍는 문제인데 하나씩 찍으면 시간초과가 난다.
카카오 2단계에 비해서 많이 쉬운 편인데 왜 난이도가 이럴까.. 흑흑
'''
import math
def solution(k, d):
    result = 0 # 결과 개수값을 의미한다.
    sero = 0
    while sero**2 <= d**2:
        value = math.floor((d**2 - sero**2) ** (0.5))
        result += value//k + 1
        sero += k
    return result