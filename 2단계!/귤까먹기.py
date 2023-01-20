# 아주 간단한 문제였으나 이상하게 생각해서 문제를 복잡하게 풀었음
# 문제의 핵심 요지를 잘 파악하고 문제를 푸는 습관이 중요함
from collections import Counter
def solution(k, tangerine):
    result = 0 
    value_list = Counter(tangerine).most_common()
    for i, v in value_list:
        result += 1
        k -= v
        if k <=0:
            break
    return result