def solution(s):
    result = []
    stack = []
    for i in s:
        if i not in stack:
            result.append(-1)
        else:
            count = 0
            for j in stack[::-1]:
                count += 1
                if i == j:
                    result.append(count)
                    break   
        stack.append(i)
    return result