from itertools import combinations
def solution(orders, course):
    answer = []
    Dic = {}
    for j in course:
        for order in orders:
            a = list(combinations(sorted(order),j))
            for alphas in a:
                word = ""
                for alpha in alphas:
                    word += alpha
                # word_temp = []
                # for alpha in alphas:
                #     word_temp.append(alpha)
                # word_temp.sort()
                # word = "".join(word_temp)
                if word not in Dic:
                    Dic[word] = 1
                else:
                    Dic[word] += 1
        print(Dic)
        l = []
        for key, value in Dic.items():
            if value > 1:
                l.append((value,key))
        if not l:
            return sorted(answer)
        l.sort(reverse = True)
        max_v = l[0][0]
        for i, v in l:
            if i == max_v:
                answer.append(v)
            else:
                break
        Dic = {}
    return sorted(answer)