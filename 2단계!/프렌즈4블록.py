# def solution(m, n, board):
#     result = 0
#     # N * N 초기값을 넣는다.
#     graph = [[0] * n for _ in range(m)]
#     for l in range(m):
#         for k in range(n):
#             graph[l][k] = board[l][k]
#     print(graph)
#     while True:
#         delete_list = []
#         # 2*2 형태를 확인한다.
#         for i in range(m-1):
#             for j in range(n-1):
#                 if graph[i][j] and graph[i][j] == graph[i+1][j] == graph[i][j+1] == graph[i+1][j+1]:
#                     for di,dj in (0,0),(0,1),(1,0),(1,1):
#                         if (i+di, j+dj) not in delete_list:
#                             delete_list.append((i+di, j+dj))
#         # 만약 삭제되는 리스트가 없다면 끝낸다.
#         if not delete_list:
#             break
#         else:
#             result += len(delete_list)
#             # 해당 부분을 삭제한다.
#             for i,j in delete_list:
#                 graph[i][j] = 0
#             # 지워진 후에 공백이 있다면 밑으로 내려온다. => 세로로 하나씩 확인하면서 0이 사이에 있다면 당겨주는 방식으로 넣어야함.
#             for j in range(n):
#                 count = 0
#                 for i in range(1,m):
#                     if not graph[i][j]:
#                         count += 1
#                         max_index = i
#                 if count != 0 or count != m:
#                     for i in range(max_index):
#                         if graph[i][j]:
#                             graph[i+count][j] = graph[i][j]
#                             graph[i][j] = 0                 
#         print(graph)              
#     return result

# N = 4
# M = 5
# board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
# print(solution(N,M,board))
N = int(input())