'''
heapq라는 것에 대해서 알 수 있었다.
만약 지속적으로 최댓값이나 최솟값을 빼야 하는 경우에는 heapq를 무조건  쓰자.
간단하게 heappush와 heappop만으로도 잘 구현할 수 있다.
'''
import heapq
def solution(n, k, enemy): # n : 병사의 수 / k : 무적권 / enemy : list형태의 적의 수
    result = 0
    heap = []
    for e in enemy:
        heapq.heappush(heap, -e)
        n -= e
        if n < 0: # visited는 음수로 들어간다.
            if k > 0:
                k -= 1
                n -= heapq.heappop(heap)
            else:
                break
        result += 1
        
    return result