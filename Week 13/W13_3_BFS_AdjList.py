"""
날짜: 2025-11-26
이름: 박용성
프로그램명: W13_3_BFS_AdjList.py
프로그램 설명: 인접 리스트와 큐를 이용한 너비 우선 탐색(BFS) 알고리즘
"""

from queue import Queue

def BFS_AL(vtx, aList, s):
    n = len(vtx)
    visited = [False]*n
    
    Q = Queue()
    Q.put(s)
    visited[s] = True
    
    while not Q.empty():
        s = Q.get()
        print(vtx[s], end=' ')
        
        for v in aList[s]:
            if visited[v] == False:
                Q.put(v)
                visited[v] = True

# --- 테스트 프로그램 ---
vtx = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
alist = [
    [1, 2],    # A
    [0, 3],    # B
    [0, 3, 4], # C
    [1, 2, 5], # D
    [2, 6, 7], # E
    [3],       # F
    [4, 7],    # G
    [4, 6]     # H
]

print('BFS_AL(출발:A): ', end=" ")
BFS_AL(vtx, alist, 0)
print()